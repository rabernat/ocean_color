import data_helpers as dh

varname = 'chl_ocx_9km'
arabian_sea = {'lon': slice(51,74), 'lat': slice(22,10)}
date_start = '1998-01-01'
date_end = '2010-12-11'

# download and save daily data
freq = 'D'
ds_daily = dh.seawifs_multi_dataset(date_start, date_end,
                                    freq='D', slice=arabian_sea)
fname = 'seawifs_Arabian_Sea_%s_%s-%s_freq-%d.nc' % (varname, date_start,
                                                     date_end, varname, freq)
ds_daily.to_netcdf(fname)

# download and save 8-day data
freq = '8D'
ds_8day = dh.seawifs_multi_dataset(date_start, date_end,
                                    freq='D', slice=arabian_sea)
fname = 'seawifs_Arabian_Sea_%s_%s-%s_freq-%d.nc' % (varname, date_start,
                                                     date_end, varname, freq)
ds_8day.to_netcdf(fname)
