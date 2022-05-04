# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
# -*- coding: utf-8 -*-
import dataiku
import pandas as pd, numpy as np
from dataiku import pandasutils as pdu

# Read recipe inputs
a = dataiku.Dataset("26698_purchase_amount_ranked_1")
adf = a.get_dataframe()



py_recipe_output = dataiku.Dataset("t")
py_recipe_output.write_with_schema(adf)



