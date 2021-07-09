# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE_MAGIC_CELL
# Automatically replaced inline charts by "no-op" charts
# %pylab inline
import matplotlib
matplotlib.use("Agg")

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
import dataiku
from dataiku import pandasutils as pdu
import pandas as pd

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
# Example: load a DSS dataset as a Pandas dataframe
mydataset = dataiku.Dataset("Corona1_partitioned")
mydataset_df = mydataset.get_dataframe()

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
#with myoutputdataset.get_writer() as writer:
for p in mydataset.list_partitions():
    #print(p)
    mydataset.read_partitions = [p]
    df = mydataset.get_dataframe()
    print(p, df.shape)
    if (p == '2021'):
        mydf = mydataset.get_dataframe()

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
# Recipe outputs
myoutputdataset = dataiku.Dataset("New_partitioned")
myoutputdataset.write_dataframe(mydf)
'''

myoutputdataset = dataiku.Dataset("New_partitioned")
with myoutputdataset.get_writer() as writer:
    for p in mydataset.list_partitions():
        #print(p)
        mydataset.read_partitions = [p]
        df = mydataset.get_dataframe()
        #print(df)

        writer.write_dataframe(df)



myoutputdataset = dataiku.Dataset("New_partitioned")
myoutputdataset.write_dataframe(df)'''