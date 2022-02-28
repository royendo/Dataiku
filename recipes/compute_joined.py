# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
# -*- coding: utf-8 -*-
import dataiku
import pandas as pd, numpy as np
from dataiku import pandasutils as pdu

# Read recipe inputs
dataset_2 = dataiku.Dataset("dataset_2")
dataset_2_df = dataset_2.get_dataframe()

dataset_1 = dataiku.Dataset("dataset_1")
dataset_1_df = dataset_1.get_dataframe()


joined_df = pd.merge(dataset_2_df,dataset_1_df,on='joining')


# Write recipe outputs
joined = dataiku.Dataset("joined")
joined.write_with_schema(joined_df)