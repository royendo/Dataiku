# -*- coding: utf-8 -*-
import dataikuapi
import pandas as pd, numpy as np
from dataiku import pandasutils as pdu

# Read recipe inputs
imports3 = dataiku.Dataset("Imports3")
imports3_df = imports3.get_dataframe()


# Compute recipe outputs
# TODO: Write here your actual code that computes the outputs
# NB: DSS supports several kinds of APIs for reading and writing data. Please see doc.
