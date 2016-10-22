# Routines for working with ocean color

## NASA's OceanColor Web

The single source for ocean color data is the website
http://oceancolor.gsfc.nasa.gov/

The available data products and their processing are described in the
[NASA Goddard Space Flight Center Ocean Data Processing System
Operations, Project Data and Software Management
Plan](http://oceancolor.gsfc.nasa.gov/cms/files/governance/odps_opdsm_plan_may2016.pdf).

Below we reproduce some of the important tables from that document.

## Data Products and Temporal Characteristics

| Sensor   | Level-1 and 2 Granule Period(s)                                                                                                    | Level-3 Compositing Periods                       |
|----------|------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------|
| CZCS     | Variable (original product size) Variable, up to 40 minutes (MLAC)                                                                 | Daily, 8 days, Monthly, Seasonal, Annual, Mission |
| OCTS     | 50 minutes (daylit orbit)                                                                                                          | Daily, 8 days, Monthly, Seasonal, Annual, Mission |
| SeaWiFS  | 40 to 43.66 minutes1 (GAC) Variable, 30 – 120 seconds (LAC) Variable, up to 15 minutes (HRPT) Variable, up to 43.66 minutes (MLAC) | Daily, 8 days, Monthly, Seasonal, Annual, Mission |
| MODIS    | 5 minutes                                                                                                                          | Daily, 8 days, Monthly, Seasonal, Annual, Mission |
| MERIS    | Variable, up to 43 minutes (RR) Variable, up to 15 minutes (FRS)                                                                   | Daily, 8 days, Monthly, Seasonal, Annual, Mission |
| Aquarius | 1 orbit (98 minutes; Level-1A includes 10 minutes overlap with adjacent orbits)                                                    | Daily, Weekly, Monthly, Seasonal, Annual          |
| VIIRS    | 6 minutes                                                                                                                          | Daily, 8 days, Monthly,Seasonal, Annual, Mission  |
| HICO     | 30 seconds                                                                                                                         | N/A                                               |
| GOCI     | 1 hour                                                                                                                             | N/A                                               |


| Product     | Data Record                              |
|-------------|------------------------------------------|
| CZCS        | October 30, 1978 to June 22, 1986        |
| OCTS        | November 1, 1996 to June 29, 1997        |
| SeaWiFS     | September 18, 1997 to December 11, 2010  |
| MODIS Terra | February 24, 2000 to present             |
| MODIS Aqua  | July 4, 2002 to present                  |
| MERIS       | April 29, 2002 to April 8, 2012          |
| Aquarius    | August 25, 2011 to June 7, 2015          |
| VIIRS       | January 2, 2012 to present               |
| HICO        | September 25, 2009 to September 13, 2014 |
| COMS        | September 25, 2009 to September 13, 2014 |


### CZCS Data Products

| Product         | Fields                                                   | Resolution |
|-----------------|----------------------------------------------------------|------------|
| Level-1A MLAC   | Raw instrument counts for all 6 CZCS bands               | 800 m      |
| Level-2 MLAC OC | Rrs (at 443, 520, 550 and 670 nm), chl-a, τ670, and K490 | 800 m      |
| Level-3 Binned  | Rrs, chl-a, τ670, and K490                               | 9 km       |
| Level-3 SMI     | Rrs, chl-a, τ670, and K490                               | 9 km       |


### OCTS Data Products

| Product         | Fields                                                | Resolution |
|-----------------|-------------------------------------------------------|------------|
| Level-1A GAC    | Raw instrument counts for all 12 OCTS bands           | 3.5 km     |
| Level-2 GAC OC  | Rrs, chl-a, τ862, Ǻ443, K490, and PIC                 | 3.5 km     |
| Level-2 GAC IOP | a, bb, aph, adg, bbp, adg-s, bbp-s, and uncertainties | 3.5 km     |
| Level-3 Binned  | Rrs, chl-a, τ862, Ǻ443, K490, PIC and IOPs.           | 9 km       |
| Level-3 SMI     | Rrs, chl-a, τ862, Ǻ443, K490, PIC and IOPs.           | 9 km       |

### SeaWiFS Data Products

| Product                        | Fields                                                           | Resolution    |
|--------------------------------|------------------------------------------------------------------|---------------|
| Level-1A GAC Level-1A MLAC     | Raw instrument counts for all 8 SeaWiFS bands                    | 4.4 Km 1.1 km |
| Level-2 GAC OC Level-2 MLAC OC | Rrs, chl-a, τ865, Ǻ443, K490, PIC, and POC                       | 4.4 km 1.1 km |
| Level-2 GAC IOP                | a, bb, aph, adg, bbp, adg-s, bbp-s, and uncertainties            | 1.1 km        |
| Level-3 Binned                 | Rrs, chl-a, τ865, Ǻ510, K490, PIC, POC, PAR, IOPs, and NDVI      | 9 km          |
| Level-3 SMI                    | Rrs, chl-a, τ865, Ǻ510, K490, PIC, POC, PAR, IOPs, LSR, and NDVI | 9 km          |

### MODIS Data Products

| Product        | Fields                                                                                                          | Resolution |
|----------------|-----------------------------------------------------------------------------------------------------------------|------------|
| Level-1A       | Raw instrument counts for all 36 MODIS bands                                                                    | 1 km       |
| Level-2 OC     | Rrs, chl-a, τ869, Ǻ443, K490, PIC, POC, PAR, and NFLH                                                           | 1 km       |
| Level-2 IOP    | a, bb, aph, adg, bbp, adg-s, bbp-s, and uncertainties                                                           | 1 km       |
| Level-2 SST    | 11 micron (day/night) and 4 micron (night only) SST                                                             | 1 km       |
| Level-3 Binned | Rrs, chl-a, τ869, Ǻ443, K490, PIC, POC, PAR, FLH, IOPs, 11 micron day SST, 11 micron night SST and 4 micron SST | 4 km       |
| Level-3 SMI    | Rrs, chl-a, τ869, Ǻ443, K490, PIC, POC, PAR, FLH, IOPs, 11 micron day SST, 11 micron night SST and 4 micron SST | 4 and 9 km |

### MERIS Data Products

| Product                      | Fields                                   | Resolution   |
|------------------------------|------------------------------------------|--------------|
| Level-1B                     | Calibrated TOA radiances for MERIS bands | 300 m        |
| Level-2 FRS OC Level-2 RR OC | Rrs, chl-a, τ865, Ǻ443, K490 and PAR     | 300 m 1.2 km |
| Level-3 Binned               | Rrs, chl-a, τ869, Ǻ443, K490 and PAR     | 4 km         |
| Level-3 SMI                  | Rrs, chl-a, τ869, Ǻ443, K490 and PAR     | 4 and 9 km   |
