# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
# -*- coding: utf-8 -*-
import dataiku
import pandas as pd, numpy as np
from dataiku import pandasutils as pdu

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
np.random.seed(0)

order_date = pd.date_range('2014-01-01 00:00:00', '2021-12-31 23:59:59', freq='min')  # For 8 years
exec_date  = pd.date_range('2014-01-02 00:00:00', '2022-01-01 23:59:59', freq='min') 
num_row = len(order_date) #  4.2M
hold_time = [np.random.randint(1, 1540000) for _ in range(num_row)]  # Random Int 
user_id = [np.random.randint(10000, 10020) for _ in range(num_row)]

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
data = {'Order_DateTime':order_date,
        'Exec_DateTime':exec_date,
        'Hold_Time':hold_time,
        'User_Id':user_id}

df = pd.DataFrame(data)

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
# Write recipe outputs
output_ds = dataiku.Dataset("work3")
output_ds.write_with_schema(df)
