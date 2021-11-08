# -*- coding: utf-8 -*-
import dataiku
import pandas as pd, numpy as np
from dataiku import pandasutils as pdu

# Read recipe inputs
date_UX_TESTS_bq_titanic_with_dates = dataiku.Dataset("DATE_UX_TESTS_bq_titanic_with_dates")
date_UX_TESTS_bq_titanic_with_dates_df = date_UX_TESTS_bq_titanic_with_dates.get_dataframe()




# Write recipe outputs
managed_folder = dataiku.Folder("iMaxicFP")
managed_folder_info = managed_folder.get_info()
