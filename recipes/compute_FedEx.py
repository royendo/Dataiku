# -*- coding: utf-8 -*-
import dataiku
import pandas as pd, numpy as np
from dataiku import pandasutils as pdu
'''
# Read recipe inputs
coronsES = dataiku.Dataset("CoronsES")
coronsES_df = coronsES.get_dataframe()


# Compute recipe outputs from inputs
# TODO: Replace this part by your actual code that computes the output, as a Pandas dataframe
# NB: DSS also supports other kinds of APIs for reading and writing data. Please see doc.

fedEx_df = coronsES_df # For this sample code, simply copy input to output


# Write recipe outputs
fedEx = dataiku.Dataset("FedEx")
fedEx.write_with_schema(fedEx_df)

'''

client = dataiku.api_client()
project = client.get_project("EVERYTHING")

# get unique value pairs on which to filter dataframe records:
dsoutname = "iprobablywillforget"
project.create_dataset(dsoutname, 'Filesystem')
# write filtered dataframe to new dataset:
dataset_out = dataiku.Dataset(dsoutname)
with dataset_out.get_writer() as writer:
    writer.write_dataframe(dataframe_out)
