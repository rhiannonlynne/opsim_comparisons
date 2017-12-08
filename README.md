# [Side-by-side comparisons summary statistics](https://oboberg.github.io/opsim_comparisons/)

A collection of sortable tables listing and comparing the summary statistics of
simulated LSST surveys.

In the the `bin` directory there is a script called  `generateCompHtml.py` that
can generate html tables similar to those linked below. Here I will show an
examples of how this script may be used from the command line.

This script does not require any of the LSST software, but you will need to
install the python packages [pandas](http://pandas.pydata.org/pandas-docs/stable/install.html) and
[bokeh](https://bokeh.pydata.org/en/latest/docs/installation.html).

Here are the options available to the script through the command line:

```
Create an interactive HTML table comparing the MAF summary statistics of a
list of runs.

positional arguments:
  baselineRun           Baseline survey for comparison

optional arguments:
  -h, --help            show this help message and exit
  --outDirs OUTDIRS [OUTDIRS ...]
                        Subdirectory containing MAF results database
  --htmlOut HTMLOUT [HTMLOUT ...]
                        Name of resulting html file.
  --runlist RUNLIST [RUNLIST ...]
                        Runs for comparisons separated by space
  --show_page           Automatically open html table in browser.
  --combine             Combine multiple subdirs into single html page.
  --comboHtml COMBOHTML
                        Name of resulting combined html file.
  --filter              Filter the summary stats to only included critical
                        values.
```

The script assumes that each run has its own directory, and within the run
directory there are subdirectories for different set of metrics.

>Example  
astro-lsst-01_2020/sci/resultsDb_sqlite.db  
astro-lsst-01_2020/sched/resultsDb_sqlite.db  
minion_1016_new_sky/sci/resultsDb_sqlite.db  
minion_1016_new_sky/sched/resultsDb_sqlite.db

#### Example 1:
Generate two html tables comparing the `sci` and `sched` results for `astro-lsst-01_2020`
and `minion_1016_new_sky`. One will be called `sci.html` and the other will be `sched.html`.

```
generateCompHtml.py minion_1016_newsky --outDirs sched sci --htmlOut sci.html sched.html --runlist
astro-lsst-01_2020  --show_page

```
#### Example 2:
Generate a html file compring the sci and sched results for astro-lsst-01_2020
and minion_1016_new_sky in a single html table.

```
generateCompHtml.py minion_1016_newsky --outDirs sci sched --comboHtml sci_sched_combo.html --runlist
astro-lsst-01_2020  --show_page --combine
```
>Note: See that only one html file is give when the `--comboHtml` flag is used.


#### Example 3:
Generate a html file compring the sci and sched results for astro-lsst-01_2020
and minion_1016_new_sky in a single html table and only include critical metrics.

```
generateCompHtml.py minion_1016_newsky --outDirs sci sched --comboHtml sci_sched_combo.html --runlist
stro-lsst-01_2020  --show_page --combine --filter
```

## Example comparisons available  here

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


## Varying Max Altitude

 Here we compare 10 year simulations where the maximum altitude angle was varied.
 

 The runs are as follows:
  - `minion-1016`:  maxalt = 86.5
  - `astro-lsst-01_2013`: maxalt = 86.5
  - `astro-lsst-01-2019`: maxalt = 80.

Clink the links below to get to the various comparison tables.

  - [Critical Metrics](https://oboberg.github.io/opsim_comparisons/MaxAlt/critical_metrics/index.html)

  - [Science Metrics](https://oboberg.github.io/opsim_comparisons/MaxAlt/science_metrics/index.html)

  - [Scheduler Metrics](https://oboberg.github.io/opsim_comparisons/MaxAlt/scheduler_metrics/index.html)