# -*- coding: utf-8 -*-
import dataiku
import pandas as pd, numpy as np
from dataiku import pandasutils as pdu

# Read recipe inputs
fitness = dataiku.Dataset("FITNESS")
fitness_df = fitness.get_dataframe()




# Write recipe outputs
s3 = dataiku.Folder("smsTHLZN")
s3_info = s3.get_info()
