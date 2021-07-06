# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
# -*- coding: utf-8 -*-
import dataiku
import pandas as pd, numpy as np
from dataiku import pandasutils as pdu

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
# Read recipe inputs
covid_jpn_total_prepared_windows_prepared = dataiku.Dataset("Corona") # 60 col
Corona_prepared_ColumnLength = dataiku.Dataset("Corona_prepared_ColumnLength") #42 col

covid_jpn_total_prepared_windows_prepared_df = covid_jpn_total_prepared_windows_prepared.get_dataframe()
df = Corona_prepared_ColumnLength.get_dataframe()
covid_jpn_total_prepared_windows_prepared
covid_jpn_total_prepared_windows_prepared.write_with_schema(df)

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
covid_jpn_total_prepared_windows_prepared

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
# Compute recipe outputs from inputs
# TODO: Replace this part by your actual code that computes the output, as a Pandas dataframe
# NB: DSS also supports other kinds of APIs for reading and writing data. Please see doc.
value = 0
covid_jpn_total_prepared_windows_prepared_df['Hosp_require'] = covid_jpn_total_prepared_windows_prepared_df['Hosp_require'].fillna(value)
covid_jpn_total_prepared_windows_prepared_df['Hosp_severe'] = covid_jpn_total_prepared_windows_prepared_df['Hosp_severe'].fillna(value)
covid_jpn_total_prepared_windows_prepared_df['Hosp_mild'] = covid_jpn_total_prepared_windows_prepared_df['Hosp_mild'].fillna(value)
covid_jpn_total_prepared_windows_prepared_df['Hosp_unknown'] = covid_jpn_total_prepared_windows_prepared_df['Hosp_unknown'].fillna(value)
covid_jpn_total_prepared_windows_prepared_df['Hosp_waiting'] = covid_jpn_total_prepared_windows_prepared_df['Hosp_waiting'].fillna(value)

# arithmetic doesnt work if the value in a dataset is null?

#covid_Japan_Python_output_df = covid_jpn_total_prepared_windows_prepared_df # For this sample code, simply copy input to output
CJP_output = covid_jpn_total_prepared_windows_prepared_df.assign(hospital_total=covid_jpn_total_prepared_windows_prepared_df.Hosp_require+
                                                                 covid_jpn_total_prepared_windows_prepared_df.Hosp_severe+
                                                                 covid_jpn_total_prepared_windows_prepared_df.Hosp_mild+
                                                                 covid_jpn_total_prepared_windows_prepared_df.Hosp_unknown+
                                                                 covid_jpn_total_prepared_windows_prepared_df.Hosp_waiting,
                                                                Positive1 = covid_jpn_total_prepared_windows_prepared_df.Positive - covid_jpn_total_prepared_windows_prepared_df.Asymptomatic

                                                                ).groupby(by="Location"
                                                                         ).agg({"hospital_total":"sum",
                                                                               "Positive1":"sum"})

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
CJP_output.head()

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
# Write recipe outputs
covid_Japan_Python_output = dataiku.Dataset("Covid_Japan_Python_output")
#covid_Japan_Python_output.write_with_schema(covid_Japan_Python_output_df)
covid_Japan_Python_output.write_with_schema(df)