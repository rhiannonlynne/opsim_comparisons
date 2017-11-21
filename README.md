# opsim_comparisons

A collection of sortable tables listing and comparing the summary statistics of
simulated LSST surveys.

You can click on any column heading to order the entire table based on that column.

Each table will include the summary statistics from `minion_1016_newsky`.

The final set of columns in each table with have a name with the following
scheme: `%_run_name` (e.g `%_colossus_2203`). These columns will contain the
absolute value of the percentage change in a summary statistic relative to
`minion_1016_newsky`.

> Example:

> CoaddM5 in `i` band in `minion_1016_newsky` = 26.402

> CoaddM5 in `i` band in `colossus_2328` = 26.509

> `%_colossus_2328 = abs([(26.402 - 26.509)/26.402]*100) = 0.403`

## OpSimV3 vs OpSimV4

A comparison of an OpsimV4 run (`colossus_2371`) with all of the new features
turned off to the previous LSST baseline (`minion_1016_newsky`) created
using OpsimV3.

`colossus_2371` had the following fetures turned off or set to zero:

- airmass bonus
- hour angle bonus
- time balancing
- restric group visits

Additionally, these tables also contains `astro-lsst-01_2013` which also had
an HA bonus = 0.5, but and HA max = 3.

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

  - [Science Metrics](https://oboberg.github.io/opsim_comparisons/hamax/science_metrics/index.html)

  - [Scheduler Metrics](https://oboberg.github.io/opsim_comparisons/hamax/scheduler_metrics/index.html)
