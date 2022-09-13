# -*- coding: utf-8 -*-
import dataiku
import pandas as pd, numpy as np
from dataiku import pandasutils as pdu

# Read recipe inputs
testcolumn_copy = dataiku.Dataset("testcolumn_copy")
testcolumn_copy_df = testcolumn_copy.get_dataframe()


# Compute recipe outputs from inputs
# TODO: Replace this part by your actual code that computes the output, as a Pandas dataframe
# NB: DSS also supports other kinds of APIs for reading and writing data. Please see doc.

test_partition_df = testcolumn_copy_df # For this sample code, simply copy input to output


# Write recipe outputs
test_partition = dataiku.Dataset("test_partition")
test_partition.write_with_schema(test_partition_df)
