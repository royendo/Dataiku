# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
# -*- coding: utf-8 -*-
import dataiku
import pandas as pd, numpy as np
from dataiku import pandasutils as pdu

# Read recipe inputs
testcolumn = dataiku.Dataset("testcolumn")
schema = testcolumn.read_schema()

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
#schema[0]['type'] = 'int'

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
testcolumn_df = testcolumn.get_dataframe()

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
# Compute recipe outputs from inputs
# TODO: Replace this part by your actual code that computes the output, as a Pandas dataframe
# NB: DSS also supports other kinds of APIs for reading and writing data. Please see doc.

columnpython_df = testcolumn_df # For this sample code, simply copy input to output


# Write recipe outputs
columnpython = dataiku.Dataset("columnpython")

columnpython.write_dataframe(columnpython_df)
columnpython.write_schema(schema)