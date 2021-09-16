# -*- coding: utf-8 -*-
import dataiku
import pandas as pd, numpy as np
from dataiku import pandasutils as pdu

# Read recipe inputs
imports3 = dataiku.Dataset("Imports3")
imports3_df = imports3.get_dataframe()


# Compute recipe outputs
# TODO: Write here your actual code that computes the outputs
# NB: DSS supports several kinds of APIs for reading and writing data. Please see doc.

o1_df = ... # Compute a Pandas dataframe to write into o1
o2_df = ... # Compute a Pandas dataframe to write into o2
o3_df = ... # Compute a Pandas dataframe to write into o3


# Write recipe outputs
o1 = dataiku.Dataset("o1")
o1.write_with_schema(o1_df)
o2 = dataiku.Dataset("o2")
o2.write_with_schema(o2_df)
o3 = dataiku.Dataset("o3")
o3.write_with_schema(o3_df)
