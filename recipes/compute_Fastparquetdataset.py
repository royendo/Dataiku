# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
# -*- coding: utf-8 -*-
import dataiku
import pandas as pd, numpy as np
import time
from dataiku import pandasutils as pdu

# Read recipe inputs
fitness_prepared = dataiku.Dataset("FITNESS_prepared")
fitness_prepared_df = fitness_prepared.get_dataframe()

time.sleep(3000)
# Compute recipe outputs from inputs
# TODO: Replace this part by your actual code that computes the output, as a Pandas dataframe
# NB: DSS also supports other kinds of APIs for reading and writing data. Please see doc.

fastparquetdataset_df = fitness_prepared_df # For this sample code, simply copy input to output


# Write recipe outputs
fastparquetdataset = dataiku.Dataset("Fastparquetdataset")
fastparquetdataset.write_with_schema(fastparquetdataset_df)