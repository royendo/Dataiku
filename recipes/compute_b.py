# -*- coding: utf-8 -*-
import dataiku
import pandas as pd, numpy as np
from dataiku import pandasutils as pdu

# Read recipe inputs
toOracle_copy = dataiku.Dataset("ToOracle_copy")
toOracle_copy_df = toOracle_copy.get_dataframe()
towritefolder = dataiku.Folder("test")
paths = towritefolder.list_paths_in_partition()
with towritefolder.get_writer("myoutputfile.txt") as w:
    w.write("some data")
# Compute recipe outputs from inputs
# TODO: Replace this part by your actual code that computes the output, as a Pandas dataframe
# NB: DSS also supports other kinds of APIs for reading and writing data. Please see doc.

b_df = toOracle_copy_df # For this sample code, simply copy input to output


# Write recipe outputs
b = dataiku.Dataset("b")
b.write_with_schema(b_df)