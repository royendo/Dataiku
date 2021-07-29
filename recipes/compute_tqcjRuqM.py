# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
# -*- coding: utf-8 -*-
import dataiku
import pandas as pd, numpy as np
from dataiku import pandasutils as pdu
import pprint 
pp = pprint.PrettyPrinter(indent=4)
# Read recipe inputs
managed_folder = dataiku.Folder("375D1F5f")
managed_folder_info = managed_folder.get_info()
managed_folder_path = managed_folder.get_path_details()

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
pp.pprint(managed_folder_info )

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
for x in managed_folder_path['children']:
    print(x['fullPath'])

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
# Write recipe outputs
toS3Bucket = dataiku.Folder("tqcjRuqM")
toS3Bucket_info = toS3Bucket.get_info()
for x in managed_folder_path['children']:
    fp = managed_folder_info['path']+x['fullPath']
# This copies a local file to the managed folder
    with open(fp) as f:
        toS3Bucket.upload_stream(x['fullPath'], f)