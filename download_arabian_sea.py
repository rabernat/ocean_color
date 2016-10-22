import data_helpers as dh
import os

varname = 'chl_ocx_9km'
arabian_sea = {'lon': slice(51,74), 'lat': slice(22,10)}
prefix = 'Seawifs_Arabian_Sea'
outdir = './data'

years = range(1998,2010)

for year in years:
    date_start = '%g-01-01' % year
    date_end = '%g-12-31' % year
    for freq in ['8D', 'D']:
        ds = dh.seawifs_multi_dataset(date_start, date_end,
                                        freq=freq, slice=arabian_sea)
        fname = '%s_%s_%g_%s.nc' % (prefix, varname, year, freq)
        print('Saving %s' % fname)
        ds.to_netcdf(os.path.join(outdir, fname))

