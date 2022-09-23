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


with folder.get_writer("myoutputfile.txt") as w:
    w.write("some data")
