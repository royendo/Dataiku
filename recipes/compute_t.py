# -*- coding: utf-8 -*-
import dataiku
import pandas as pd, numpy as np
from dataiku import pandasutils as pdu

# Read recipe inputs
26698_purchase_amount_ranked_1 = dataiku.Dataset("26698_purchase_amount_ranked_1")
26698_purchase_amount_ranked_1_df = 26698_purchase_amount_ranked_1.get_dataframe()


# Compute recipe outputs from inputs
# TODO: Replace this part by your actual code that computes the output, as a Pandas dataframe
# NB: DSS also supports other kinds of APIs for reading and writing data. Please see doc.

t_df = 26698_purchase_amount_ranked_1_df # For this sample code, simply copy input to output


# Write recipe outputs
t = dataiku.Dataset("t")
t.write_with_schema(t_df)
