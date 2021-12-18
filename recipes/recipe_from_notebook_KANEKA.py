# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE_MAGIC_CELL
# Automatically replaced inline charts by "no-op" charts
# %pylab inline
import matplotlib
matplotlib.use("Agg")

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
from dataiku import SQLExecutor2

executor = SQLExecutor2(connection="PostgreSQL") # or dataset="dataset_name"

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE

df = executor.query_to_df('SELECT * FROM "public"."DKU_TUTORIAL_PARTITIONED_MODELS_partitioned_postgre"')

# df is a Pandas dataframe with two columns : "col1" and "count"

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
# Recipe outputs
no_input_python_sqlserver = dataiku.Dataset("no_input_python_sqlserver")
no_input_python_sqlserver.write_with_schema(pandas_dataframe)