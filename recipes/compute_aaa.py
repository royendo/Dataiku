# -*- coding: utf-8 -*-
import dataiku
import pandas as pd, numpy as np
from dataiku import pandasutils as pdu
import time

# Read recipe inputs
filesystem = dataiku.Folder("qWeVti46")
filesystem_info = filesystem.get_info()

time.sleep(3000)

# Compute recipe outputs
# TODO: Write here your actual code that computes the outputs
# NB: DSS supports several kinds of APIs for reading and writing data. Please see doc.

aaa_df = ... # Compute a Pandas dataframe to write into aaa


# Write recipe outputs
aaa = dataiku.Dataset("aaa")
aaa.write_with_schema(aaa_df)
