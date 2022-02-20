# -*- coding: utf-8 -*-
import dataiku
import pandas as pd, numpy as np
from dataiku import pandasutils as pdu

# Read recipe inputs
testa = dataiku.Folder("n4rNwq77")
testa_info = testa.get_info()


# Compute recipe outputs
# TODO: Write here your actual code that computes the outputs
# NB: DSS supports several kinds of APIs for reading and writing data. Please see doc.

wow_df = ... # Compute a Pandas dataframe to write into wow


# Write recipe outputs
wow = dataiku.Dataset("wow")
wow.write_with_schema(wow_df)
