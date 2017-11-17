# opsim_comparisons

A collection of sortable tables listing and comparing the summary statistics of
simulated LSST surveys.

Each table will include the summary statistics from `minion_1016_newsky`.

The final set of columns in each table with have a name with the following
scheme: `%_run_name` (e.g `%_colossus_2203`). These columns will contain the
absolute value of the percentage change in a summary statistic relative to
`minion_1016_newsky`.

> Example:

> CoaddM5 in `i` band in `minion_1016_newsky` = 26.402

> CoaddM5 in `i` band in `colossus_2328` = 26.509

> `%_colossus_2328 = abs([(26.402 - 26.509)/26.402]*100) = 0.403`



## Varying Hour Angle Bonus

Here we compare 10 year simulations where the hour angle bonus was increased.  
They all have an airmass bonus set to zero.

The runs are as follows:
 - `colossus_2328`: HA bonus = 0.05
 - `colossus_2399`: HA bonus = 0.50
 - `colossus_2378`: HA bonus = 0.80

Additionally, this table also contains `astro-lsst-01_2013` which also had
an HA bonus = 0.5, but and HA max = 3.

Clink the links below to get to the various comparison tables.

 - [Science Metrics](https://oboberg.github.io/opsim_comparisons/hour_anlgle_bonus/science_metrics/index.html)

 - [Scheduler Metrics](https://oboberg.github.io/opsim_comparisons/hour_anlgle_bonus/scheduler_metrics/index.html)
