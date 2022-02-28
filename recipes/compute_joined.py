# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
# -*- coding: utf-8 -*-
import dataiku
import pandas as pd, numpy as np
from dataiku import pandasutils as pdu

# Read recipe inputs
dataset_2 = dataiku.Dataset("dataset_2")
dataset_2_df = dataset_2.get_dataframe()
dataset_2_df.dataset_2_col.astype(object)

dataset_1 = dataiku.Dataset("dataset_1")
dataset_1_df = dataset_1.get_dataframe()
dataset_1_df.joining.astype(str)




# Compute recipe outputs
# TODO: Write here your actual code that computes the outputs
# NB: DSS supports several kinds of APIs for reading and writing data. Please see doc.

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
dataset_2_df

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
dataset_1_df.dtypes

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE

joined_df = dataset_2_df.join(dataset_1_df)[source]


# Write recipe outputs
joined = dataiku.Dataset("joined")
joined.write_with_schema(joined_df)