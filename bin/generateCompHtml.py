#!/usr/bin/env python

import os
import argparse
import numpy as np
import pandas as pd
import sqlite3
from functools import reduce
from bokeh.models import CustomJS
from bokeh.io import output_file
from bokeh.layouts import widgetbox, layout, row, column
from bokeh.models import ColumnDataSource
from bokeh.models.widgets import DataTable, DateFormatter, TableColumn, NumberFormatter, Select
from bokeh.plotting import Figure, output_file, show

def summaryDiffReport(baselineRun, outDir, runlist, percent_threshold = None):
    """
    Read and merge MAF results databases for opsim a series of runs and compare
    the summary statistics in each run to the same values in a baseline run.

    For the statistics that match in each run to the baseline run, a percent
    change change is calculated relative to the values in the baseline run.

    This percent change is calculated in the following way:

    %_run = abs((value_run - value_baseline) / value_run)*100



    Parameters
    ----------
    baselineRun : str
        The is the run that will serve as the basis for the comparisons between
        the runs.

    outDir : list
        List of directories containing the results databases for the runs that
        will be compared

    runlist : list
        List of of runs to compare.

    percent_threshold: float, opt
        A minimum threshold to only include summary statistics that had a
        percent change greater than or equal to this value.

    Returns
    -------
    pandas Dataframe

    """

    path_baseline = os.path.join(baselineRun, outDir, 'resultsDb_sqlite.db')

    results1_db = sqlite3.connect(path_baseline)
    df_metrics_1 = pd.read_sql_query("select * from metrics",results1_db)

    avoid_metrics = ['Histogram','3Sigma','%ile','Rms','Min','Max']
    pattern = '|'.join(avoid_metrics)
    df_metrics_1 = df_metrics_1[(df_metrics_1.metricName.str.contains(pattern))==False]

    df_summary_stats_1 = pd.read_sql_query("select * from summarystats",results1_db)
    df_metrics_1 = df_metrics_1[df_metrics_1.metricId.isin(df_summary_stats_1.metricId) == True]

    dataframes = [None] * len(runlist)
    cols = ['metricName','metricMetadata','summaryName','slicerName','fullName',baselineRun]
    for p, run in enumerate(runlist):
        runpath = os.path.join(run, outDir, 'resultsDb_sqlite.db')
        output_df = pd.DataFrame()
        results2_db = sqlite3.connect(runpath)
        df_metrics_2 = pd.read_sql_query("select * from metrics",results2_db)
        df_metrics_2 = df_metrics_2[df_metrics_2.metricName.str.contains(pattern) == False]


        df_summary_stats_2 = pd.read_sql_query("select * from summarystats",results2_db)
        df_metrics_2 = df_metrics_2[df_metrics_2.metricId.isin(df_summary_stats_2.metricId) == True]

        in_common_metrics = df_metrics_1.merge(df_metrics_2,on=['metricName','slicerName','metricMetadata'],
                                               how="inner")

        avoid_summarys = ['3Sigma','Rms','Min','Max','RobustRms','%ile']
        summary_pattern = '|'.join(avoid_summarys)

        df_summary_stats_1 = df_summary_stats_1[(df_summary_stats_1['summaryName'].str.contains(summary_pattern))==False]
        df_summary_stats_2 = df_summary_stats_2[df_summary_stats_2['summaryName'].str.contains(summary_pattern)==False]

        metricNames = []
        metricMetaData = []
        slicerName = []
        summaryName = []
        summaryValues_1 = []
        summaryValues_2 = []
        for i, (metid_x, metid_y) in enumerate(zip(in_common_metrics.metricId_x,in_common_metrics.metricId_y)):
            if len(df_summary_stats_1[df_summary_stats_1.metricId == metid_x].summaryValue.values) == 1:
                metricNames.append(in_common_metrics.metricName.iloc[i])
                metricMetaData.append(in_common_metrics.metricMetadata.iloc[i])
                slicerName.append(in_common_metrics.slicerName.iloc[i])
                summaryName.append(df_summary_stats_1[df_summary_stats_1.metricId == metid_x].summaryName.values[0])
                summaryValues_1.append(df_summary_stats_1[df_summary_stats_1.metricId == metid_x].summaryValue.values[0])
                summaryValues_2.append(df_summary_stats_2[df_summary_stats_2.metricId == metid_y].summaryValue.values[0])
            if len(df_summary_stats_1[df_summary_stats_1.metricId == metid_x].summaryValue.values) > 1:
                for j,value in enumerate(df_summary_stats_1[df_summary_stats_1.metricId == metid_x].summaryValue.values):
                    metricNames.append(in_common_metrics.metricName.iloc[i])
                    metricMetaData.append(in_common_metrics.metricMetadata.iloc[i])
                    slicerName.append(in_common_metrics.slicerName.iloc[j])
                    summaryName.append(df_summary_stats_1[df_summary_stats_1.metricId == metid_x].summaryName.values[j])
                    summaryValues_1.append(df_summary_stats_1[df_summary_stats_1.metricId == metid_x].summaryValue.values[j])
                    summaryValues_2.append(df_summary_stats_2[df_summary_stats_2.metricId == metid_y].summaryValue.values[j])


        output_df['metricName'] = metricNames
        output_df['metricMetadata'] = metricMetaData
        output_df['slicerName'] = slicerName
        output_df['summaryName'] = summaryName
        output_df[baselineRun] = summaryValues_1
        output_df[run] = summaryValues_2
        percent_change = ((np.array(summaryValues_2) - np.array(summaryValues_1))/np.array(summaryValues_2))*100
        output_df['%'+'_'+run] = np.abs(percent_change)

        if percent_threshold is not None:
            output_df = output_df[(np.abs(output_df.percent_change) >= percent_threshold)]
        dataframes[p] = output_df

    df_final = reduce(lambda left,right: pd.merge(left,right,
                                                  on= ['metricName','slicerName',
                                                       'metricMetadata',
                                                       baselineRun,
                                                       'summaryName'],
                                                  how='inner'), dataframes)
    df_final['fullName'] = df_final.metricName+' '+df_final.metricMetadata+' '+df_final.summaryName

    for run in runlist:
        cols.append(run)
    for run in runlist:
        cols.append('%'+'_'+run)
    df_final = df_final[cols]
    return df_final

def filterMetrics(dataframe, metricList = None):
    """
    Filter the set of summary stats in the resulting combined dataframe based on the
    full name of the metric. That is `metricName`, `metricMetadata`, and
    `summaryName`.

    Parameters
    ----------
    dataframe : pandas dataframe
        The combined summary stats dataframe.
    metricList : list, opt
        List of the metrics that would like in include in the final dataframe.
        If this is `None` the astronomer's eye/critical metrics will be used.

    Returns
    -------
    pandas dataframe
        This dataframe will only include the summary stats present in the
            `metricList`.
    """

    if metricList is None:
        metricList = ['NVisits All Visits Count',
                      'NVisits Per night Median',
                      'Nights with observations All Visits (days)',
                      'Total effective time of survey All Visits (days)',
                      'fO All Visits (non-dithered) fOArea: Nvisits (#)',
                      'fO All Visits (non-dithered) fONv: Area (sqdeg)',
                      'OpenShutterFraction Per night Median',
                      'Median slewTime All Visits Identity',
                      'Median normairmass all band, all props Identity',
                      'NVisits WFD Fraction of total',
                      'Filter Changes Per night Mean',
                      'Median airmass r band, WFD Median',
                      'Median airmass i band, WFD Median',
                      'Fraction of revisits faster than 30.0 minutes All Visits (non-dithered) Area (sq deg)',
                      'Fraction of revisits faster than 30.0 minutes All Visits (non-dithered) Median']
    else:
        metricList = metricList

    pattern = '|'.join(metricList)
    dataframe = dataframe [(dataframe['fullName'].isin(metricList) == True)]

    return dataframe

def generateDiffHtml(dataframe, html_out, show_page = False):
    """
    Use `bokeh` to convert the dataframe returned by `summaryDiffReport` into
    an interactive html table.

    Parameters
    ----------
    dataframe : pandas DataFrame
        Dataframe containg the summary stats of multpile opsim runs.

    html_out : str
        Name of the html that will be output and saved.

    show_page : bool, opt
        If True the html page generate by this function will automatically open
        in your browser

    """
    output_file(html_out, title = html_out.strip('.html'))

    columns = []

    for col in dataframe.columns:

        if col not in ['metricName','metricMetadata','summaryName','slicerName','fullName']:
            columns.append(TableColumn(field=col, title=col, formatter=NumberFormatter(format="0.0000")))
        else:
            columns.append(TableColumn(field=col, title=col))
    source = ColumnDataSource(dataframe)
    original_source = ColumnDataSource(dataframe)
    data_table = DataTable(source=source, columns=columns, width=1700, height=2000)

    combined_callback_code = """
    var data = source.get('data');
    var original_data = original_source.get('data');
    var metricName = metricName_select_obj.get('value');
    var metricMetadata = metricMetadata_select_obj.get('value');
    var summaryName = summaryName_select_obj.get('value');

     for (var key in original_data) {
         data[key] = [];
         for (var i = 0; i < original_data['metricName'].length; ++i) {
             if ((metricName === "ALL" || original_data['metricName'][i] === metricName) &&
                 (metricMetadata === "ALL" || original_data['metricMetadata'][i] === metricMetadata) &&
                 (summaryName === "ALL" || original_data['summaryName'][i] === summaryName)) {
                 data[key].push(original_data[key][i]);
             }
         }
     }
    source.trigger('change')
    target_obj.trigger('change');
    """

    metricName_list = ['ALL'] + dataframe['metricName'].unique().tolist()
    metricName_select = Select(title="metricName:", value=metricName_list[0], options=metricName_list)

    metricMetadata_list = ['ALL'] + dataframe['metricMetadata'].unique().tolist()
    metricMetadata_select = Select(title="metricMetadata:",
                                   value=metricMetadata_list[0],
                                   options=metricMetadata_list)

    summaryName_list = ['ALL'] + dataframe['summaryName'].unique().tolist()
    summaryName_select = Select(title="summaryName:",
                                value=summaryName_list[0],
                                options=summaryName_list)


    generic_callback = CustomJS(args=dict(source=source,
                                          original_source=original_source,
                                          metricName_select_obj=metricName_select,
                                          metricMetadata_select_obj=metricMetadata_select,
                                          summaryName_select_obj=summaryName_select,
                                          target_obj=data_table),
                                code=combined_callback_code)

    metricName_select.callback = generic_callback
    metricMetadata_select.callback = generic_callback
    summaryName_select.callback = generic_callback



    dropdownMenus = column([metricName_select, metricMetadata_select, summaryName_select])
    page_layout = layout([dropdownMenus,data_table])
    if show_page is True:
        show(page_layout)


def parseArgs():
    parser = argparse.ArgumentParser(description="Create an interactive HTML table comparing the MAF summary statistics of a list of runs.")

    parser.add_argument("baselineRun", type=str, help="Baseline survey for comparison")
    parser.add_argument("--outDirs", nargs='+',type=str, help="Subdirectory containing MAF results database")
    parser.add_argument("--htmlOut", nargs='+',type=str, help="Name of resulting html file.")
    parser.add_argument('--runlist', nargs='+', default=None, help='Runs for comparisons separated by space')
    parser.add_argument('--show_page', dest='show_page', action='store_true',
                        default=False, help="Automatically open html table in browser.")
    parser.add_argument('--combine', dest='combine', action='store_true',
                        default=False, help="Combine multiple subdirs into single html page.")
    parser.add_argument("--comboHtml", default = None ,type=str, help="Name of resulting combined html file.")
    parser.add_argument('--filter', dest='filter', action='store_true',
                        default=False, help="Filter the summary stats to only included critical values.")
    parser.add_argument('--savedf', default = None, type=str, help="Name of csv file to save dataframe")

    args = parser.parse_args()
    return args


if __name__ == '__main__':
    args = parseArgs()
    df_list = []

    for d in args.outDirs:
        df_final = summaryDiffReport(args.baselineRun, d, args.runlist)
        if args.filter is True:
            df_final = filterMetrics(df_final)
        df_list.append(df_final)

    if args.combine is False:
        for i,h in enumerate(args.htmlOut):
            generateDiffHtml(df_list[i], h, show_page = args.show_page)
    else:
        combine_df = pd.concat(df_list, ignore_index =True)
        generateDiffHtml(combine_df, args.comboHtml, show_page = args.show_page)
        if args.savedf is not None:
            combine_df.to_csv(args.savedf, index = False)
