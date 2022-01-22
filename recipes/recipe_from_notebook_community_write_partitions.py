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
print "I am working for year %s" % (dataiku.dku_flow_variables["DKU_DST_YEAR"])