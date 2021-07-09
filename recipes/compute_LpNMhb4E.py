# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
# -*- coding: utf-8 -*-
import dataiku
import pandas as pd, numpy as np
from dataiku import pandasutils as pdu

# Read recipe inputs
corona1 = dataiku.Dataset("Corona1")
corona1_df = corona1.get_dataframe()




# Write recipe outputs
folder = dataiku.Folder("LpNMhb4E")
paths = folder.list_paths_in_partition()
with folder.get_writer("myoutputfile.txt") as w:
    w.write("some data")