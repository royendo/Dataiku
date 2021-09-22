# -*- coding: utf-8 -*-
import dataiku
import pandas as pd, numpy as np
from dataiku import pandasutils as pdu

# Read recipe inputs
community = dataiku.Dataset("community")
community_df = community.get_dataframe()


# Compute recipe outputs from inputs
# TODO: Replace this part by your actual code that computes the output, as a Pandas dataframe
# NB: DSS also supports other kinds of APIs for reading and writing data. Please see doc.

communitypython_df = community_df # For this sample code, simply copy input to output


# Write recipe outputs
communitypython = dataiku.Dataset("communitypython")
communitypython.write_with_schema(communitypython_df)
