# -*- coding: utf-8 -*-
import dataiku
import pandas as pd, numpy as np
from dataiku import pandasutils as pdu

# Read recipe inputs
toS3Bucket = dataiku.Folder("tqcjRuqM")
toS3Bucket_info = toS3Bucket.get_info()


# Compute recipe outputs
# TODO: Write here your actual code that computes the outputs
# NB: DSS supports several kinds of APIs for reading and writing data. Please see doc.

fastparquet_df = ... # Compute a Pandas dataframe to write into Fastparquet


# Write recipe outputs
fastparquet = dataiku.Dataset("Fastparquet")
fastparquet.write_with_schema(fastparquet_df)
