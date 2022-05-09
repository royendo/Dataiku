# -*- coding: utf-8 -*-
import dataiku
import pandas as pd, numpy as np
from dataiku import pandasutils as pdu

# Read recipe inputs
no_auto_test = dataiku.Dataset("no-auto-test")
no_auto_test_df = no_auto_test.get_dataframe()




# Write recipe outputs
test = dataiku.Folder("PExuz1em")
test_info = test.get_info()
