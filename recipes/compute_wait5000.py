# -*- coding: utf-8 -*-
import dataiku
import pandas as pd, numpy as np
from dataiku import pandasutils as pdu
import time 
# Read recipe inputs
xlsx_copy = dataiku.Dataset("xlsx_copy")
xlsx_copy_df = xlsx_copy.get_dataframe()

time.wait(50000)
# Compute recipe outputs from inputs
# TODO: Replace this part by your actual code that computes the output, as a Pandas dataframe
# NB: DSS also supports other kinds of APIs for reading and writing data. Please see doc.

wait5000_df = xlsx_copy_df # For this sample code, simply copy input to output


# Write recipe outputs
wait5000 = dataiku.Dataset("wait5000")
wait5000.write_with_schema(wait5000_df)
