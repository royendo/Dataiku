# -*- coding: utf-8 -*-
import dataiku
import pandas as pd, numpy as np
from dataiku import pandasutils as pdu

# Read recipe inputs
tests = dataiku.Folder("iV6c3jWU")
tests_info = tests.get_info()


# Write recipe outputs
folder = dataiku.Folder("oQL0pTOm")
folder_info = folder.get_info()


# target_folder will now contain a copy of all files that were in source_folder
future = tests.copy_to(folder)
future.wait_for_result()