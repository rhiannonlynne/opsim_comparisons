# Side-by-side comparisons summary statistics

A collection of sortable tables listing and comparing the summary statistics of
simulated LSST surveys.

There are currently 3 tables for each set of runs.

 - Critical metrics (a sample of SRD and astronomer's eye metrics)
 - Science metrics (metrics run by the validateScience MAF script)
 - Scheduler metrics (metrics run by the validateScheduler MAF script)

You can click on any column heading to order the entire table based on that column.

Additionally, at the top of each table there will be 3 drop down menus:
`metricNames`, `metriMetaData`, and `summaryName`. Clicking on any one of
these menus will bring up all of the available options in the table. You can
choose any single combination of the three options to filter the table.

> Note: These
menus are not synced to one another, so if your selections bring up a blank table
it is a combination that does not exist in the table.

Each table will include the summary statistics from `minion_1016_newsky`.

The final set of columns in each table with have a name with the following
scheme: `%_run_name` (e.g `%_colossus_2203`). These columns will contain the
absolute value of the percentage change in a summary statistic relative to
`minion_1016_newsky`.

> Example:  
CoaddM5 in `i` band in `minion_1016_newsky` = 26.402  
CoaddM5 in `i` band in `colossus_2328` = 26.509  
`%_colossus_2328 = abs([(26.402 - 26.509)/26.402]*100) = 0.403`



## OpSimV3 vs OpSimV4

A comparison of an OpsimV4 run (`astro-lsst-01_2020`) with all of the new features
turned off to the previous LSST baseline (`minion_1016_newsky`) created
using OpsimV3.

`astro-lsst-01_2020` had the following features turned off or set to zero:

- airmass bonus
- hour angle bonus
- time balancing
- restrict group visits

Clink the links below to get to the various comparison tables.

 - [Critical Metrics](https://oboberg.github.io//opsim_comparisons/v3_v4/critical_metrics/index.html)

 - [Science Metrics](https://oboberg.github.io//opsim_comparisons/v3_v4/science_metrics/index.html)

 - [Scheduler Metrics](https://oboberg.github.io/opsim_comparisons/v3_v4/scheduler_metrics/index.html)


## Varying Hour Angle Bonus

Here we compare 10 year simulations where the hour angle bonus was increased.  
They all have an airmass bonus set to zero.

The runs are as follows:
 - `colossus_2328`: HA bonus = 0.05
 - `colossus_2399`: HA bonus = 0.50
 - `colossus_2378`: HA bonus = 0.80

Additionally, these tables also contains `astro-lsst-01_2013` which also had
an HA bonus = 0.5, but and HA max = 3.

Clink the links below to get to the various comparison tables.

 - [Critical Metrics](https://oboberg.github.io/opsim_comparisons/hour_anlgle_bonus/critical_metrics/index.html)

 - [Science Metrics](https://oboberg.github.io/opsim_comparisons/hour_anlgle_bonus/science_metrics/index.html)

 - [Scheduler Metrics](https://oboberg.github.io/opsim_comparisons/hour_anlgle_bonus/scheduler_metrics/index.html)


## Varying HA max

 Here we compare 10 year simulations where the maximum Hour angle was varied.
 > Note: For the deep drilling fields HA max is still set to 6.

 The runs are as follows:
  - `colossus_2414`: HA max = 2, HA bonus = 0.05
  - `astro-lsst-01_2013`: HA max = 3, HA bonus = 0.50
  - `colossus_2421`: HA max = 4, HA bonus = 0.50
  - `colossus_2399`: HA max = 6, HA bonus = 0.50

Clink the links below to get to the various comparison tables.

  - [Critical Metrics](https://oboberg.github.io/opsim_comparisons/hamax/critical_metrics/index.html)

  - [Science Metrics](https://oboberg.github.io/opsim_comparisons/hamax/science_metrics/index.html)

  - [Scheduler Metrics](https://oboberg.github.io/opsim_comparisons/hamax/scheduler_metrics/index.html)
