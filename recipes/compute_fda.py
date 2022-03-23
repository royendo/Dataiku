# -*- coding: utf-8 -*-
import dataiku
import pandas as pd, numpy as np
from dataiku import pandasutils as pdu

# Read recipe inputs
tesaa = dataiku.Folder("YIvPpqVC")
tesaa_info = tesaa.get_info()


# Compute recipe outputs
# TODO: Write here your actual code that computes the outputs
# NB: DSS supports several kinds of APIs for reading and writing data. Please see doc.

fda_df = ... # Compute a Pandas dataframe to write into fda


# Write recipe outputs
fda = dataiku.Dataset("fda")
fda.write_with_schema(fda_df)
