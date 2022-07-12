# -*- coding: utf-8 -*-
import dataiku
import pandas as pd, numpy as np
from dataiku import pandasutils as pdu

# Read recipe inputs
active_employees_prepared = dataiku.Dataset("active_employees_prepared")
active_employees_prepared_df = active_employees_prepared.get_dataframe()


# Compute recipe outputs from inputs
# TODO: Replace this part by your actual code that computes the output, as a Pandas dataframe
# NB: DSS also supports other kinds of APIs for reading and writing data. Please see doc.

s3_active_df = active_employees_prepared_df # For this sample code, simply copy input to output


# Write recipe outputs
s3_active = dataiku.Dataset("s3_active")
s3_active.write_with_schema(s3_active_df)
