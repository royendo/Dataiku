# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE_MAGIC_CELL
# Automatically replaced inline charts by "no-op" charts
# %pylab inline
import matplotlib
matplotlib.use("Agg")

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
import dataiku
import dataiku.spark as dkuspark
import pyspark
from pyspark.sql import SQLContext

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
# Load PySpark
sc = pyspark.SparkContext.getOrCreate()
sqlContext = SQLContext(sc)

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
# Example: Read the descriptor of a Dataiku dataset
mydataset = dataiku.Dataset("mydataset")
# And read it as a Spark dataframe
df = dkuspark.get_dataframe(sqlContext, mydataset)

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
# Example: Get the count of records in the dataframe
df.count()