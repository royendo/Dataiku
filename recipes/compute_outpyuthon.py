# -*- coding: utf-8 -*-
import dataiku
import pandas as pd, numpy as np
from dataiku import pandasutils as pdu

# Read recipe inputs
managed_folder = dataiku.Folder("375D1F5f")
managed_folder_info = managed_folder.get_info()


# Compute recipe outputs
# TODO: Write here your actual code that computes the outputs
# NB: DSS supports several kinds of APIs for reading and writing data. Please see doc.

outpyuthon_df = ... # Compute a Pandas dataframe to write into outpyuthon


# Write recipe outputs
outpyuthon = dataiku.Dataset("outpyuthon")
outpyuthon.write_with_schema(outpyuthon_df)
