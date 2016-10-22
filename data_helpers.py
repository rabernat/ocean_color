import numpy as np
import xarray as xr
import pandas as pd
from datetime import datetime, timedelta
from warnings import warn
from tqdm import tqdm
import time

def seawifs_opendap_url(date, varname='chl_ocx_9km', freq='DAY'):
    baseurl = 'http://oceandata.sci.gsfc.nasa.gov/opendap/SeaWiFS/L3SMI'
    level = 'L3m'
    suffix = 'nc'

    year = date.strftime('%Y')
    daynum = date.strftime('%j')
    if freq=='DAY':
        daterange = 'S%s%s' % (year, daynum)
        prefix = 'DAY_CHL'
    elif freq=='8D':
        date_next = date + timedelta(days=7)
        # the intervals don't cross year
        if date_next.year != date.year:
            date_next = datetime(date.year,12,31)
        daterange = 'S%s%s%s%s' % (year, daynum,
                                   date_next.strftime('%Y'),
                                   date_next.strftime('%j'))
        prefix = '8D_CHL'
    else:
        raise ValueError("`freq` must be 'DAY' or '8D'")
    url = '%s/%s/%s/%s.%s_%s_%s.%s' % (baseurl, year, daynum, daterange, level, prefix, varname, suffix)
    return(url)

def seawifs_dataset(date, slice={}, varname='chl_ocx_9km', freq='DAY'):
    url = seawifs_opendap_url(date, varname, freq)
    ds = xr.open_dataset(url)
    ds = ds.sel(**slice)
    ds.load()
    return ds

def seawifs_multi_dataset(date_start, date_end, freq='D',
                          slice={}, varname='chl_ocx_9km',
                          retries=10, sleep=1.):
    """Get a timeseries of seawifs data from a certain region.

    PARAMETERS
    ----------
    date_date, date_end : str
        ISO dates for start and end of timeseries (e.g. '2001-01-01')
    freq : {'D', '8D'}
        Temporal frequency desired (one day or eight days)
    slice : dict
        Slices used to index the dataset
        (e.g. {'lon': slice(51,74), 'lat': slice(22,10)})
    varname : str
        The seawifs variable to read
    retries : int
        Number of times to rety opendap downloads
    sleep : float
        How long to wait between retries

    RETURNS
    -------
    ds : xarray.Dataset
    """
    assert freq in ['D', '8D']
    date_range = pd.date_range(start=date_start, end=date_end,
                               freq=freq).rename('time')
    # seawifs use a different convention for frequency
    if freq=='D':
        freq = 'DAY'

    datasets = []

    for date in tqdm(date_range):
        for n in range(retries):
            success=False
            try:
                ds = seawifs_dataset(date, slice, freq=freq, varname=varname)
                success=True
                break
            except RuntimeError:
                time.sleep(sleep)
        if not success:
            warn("Couldn't load dataset " +
                 seawifs_opendap_url(date, freq=freq, varname=varname))
            # use a dataset full of nans
            ds = np.nan * ds
        datasets.append(ds)

    return xr.concat(datasets, dim=date_range)
