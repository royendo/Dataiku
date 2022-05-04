# -*- coding: utf-8 -*-
import dataiku
import pandas as pd, numpy as np
from dataiku import pandasutils as pdu

# Read recipe inputs
26698_purchase_amount_ranked_1 = dataiku.Dataset("26698_purchase_amount_ranked_1")
26698_purchase_amount_ranked_1_df = 26698_purchase_amount_ranked_1.get_dataframe()
