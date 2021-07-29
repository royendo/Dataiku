# -*- coding: utf-8 -*-
import dataiku
import pandas as pd, numpy as np
from dataiku import pandasutils as pdu

# Read recipe inputs
s3 = dataiku.Folder("pCkKYlgx")
s3_info = s3.get_info()




# Write recipe outputs
local_folder = dataiku.Folder("YJppbQ7k")
local_folder_info = local_folder.get_info()
