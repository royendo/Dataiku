# -*- coding: utf-8 -*-
import dataiku
import pandas as pd, numpy as np
from dataiku import pandasutils as pdu

# Read recipe inputs
out_s0 = dataiku.Dataset("out_s0")
out_s0_df = out_s0.get_dataframe()


# Compute recipe outputs from inputs
# TODO: Replace this part by your actual code that computes the output, as a Pandas dataframe
# NB: DSS also supports other kinds of APIs for reading and writing data. Please see doc.

out_df = out_s0_df # For this sample code, simply copy input to output


# Write recipe outputs
out = dataiku.Dataset("out")
out.write_with_schema(out_df)
