# -*- coding: utf-8 -*-
import dataiku
import pandas as pd, numpy as np
from dataiku import pandasutils as pdu

# Read recipe inputs
managed_folder = dataiku.Folder("375D1F5f")
managed_folder_info = managed_folder.get_info()




# Write recipe outputs
toS3Bucket = dataiku.Folder("tqcjRuqM")
toS3Bucket_info = toS3Bucket.get_info()

\\\
