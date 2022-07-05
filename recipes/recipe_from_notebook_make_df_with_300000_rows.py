# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
import pandas as pd
import dataiku

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
row = []
for i in range(300000):
    row.append(['x', i])
print(row)

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
df = pd.DataFrame(row, columns=["X", "Value"])

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
df

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE

py_recipe_output = dataiku.Dataset("dataset")
py_recipe_output.write_with_schema(df)
