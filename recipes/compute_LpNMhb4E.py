# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
# -*- coding: utf-8 -*-
import dataiku
import pandas as pd, numpy as np
from dataiku import pandasutils as pdu

# Read recipe inputs
#corona1 = dataiku.Dataset("Corona1")
#corona1_df = corona1.get_dataframe()




# Write recipe outputs
folder = dataiku.Folder("LpNMhb4E")
paths = folder.list_paths_in_partition()
with folder.get_writer("myoutputfile.txt") as w:
    w.write("some, data")
    w.write("\n")
    w.write("1, 3")
    
    # Write recipe outputs
folder = dataiku.Folder("Ml0oF4Xt")
paths = folder.list_paths_in_partition()
with folder.get_writer("myoutputfile.txt") as w:
    w.write("some data")
    
    # Write recipe outputs
folder = dataiku.Folder("gHvabmHo")
paths = folder.list_paths_in_partition()
with folder.get_writer("myoutputfile.txt") as w:
    w.write("some data")