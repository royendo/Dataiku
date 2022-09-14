# -*- coding: utf-8 -*-
import dataiku
import pandas as pd, numpy as np
from dataiku import pandasutils as pdu
import time

# Read recipe inputs
xlsx = dataiku.Dataset("xlsx")
xlsx_df = xlsx.get_dataframe()


#time.sleep(3000)
# Compute recipe outputs from inputs
# TODO: Replace this part by your actual code that computes the output, as a Pandas dataframe
# NB: DSS also supports other kinds of APIs for reading and writing data. Please see doc.

xlsx_wait_df = xlsx_df # For this sample code, simply copy input to output


# Write recipe outputs
xlsx_wait = dataiku.Dataset("xlsx_wait")
xlsx_wait.write_with_schema(xlsx_wait_df)
