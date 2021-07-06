# -*- coding: utf-8 -*-
import dataiku
import pandas as pd, numpy as np
from dataiku import pandasutils as pdu

# Read recipe inputs
covid_jpn_total_prepared_windows_prepared = dataiku.Dataset("covid_jpn_total_prepared_windows_prepared")
covid_jpn_total_prepared_windows_prepared_df = covid_jpn_total_prepared_windows_prepared.get_dataframe()


# Compute recipe outputs from inputs
# TODO: Replace this part by your actual code that computes the output, as a Pandas dataframe
# NB: DSS also supports other kinds of APIs for reading and writing data. Please see doc.

covid_Japan_Python_output_df = covid_jpn_total_prepared_windows_prepared_df # For this sample code, simply copy input to output


# Write recipe outputs
covid_Japan_Python_output = dataiku.Dataset("Covid_Japan_Python_output")
covid_Japan_Python_output.write_with_schema(covid_Japan_Python_output_df)
