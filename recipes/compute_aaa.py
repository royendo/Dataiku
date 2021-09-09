# -*- coding: utf-8 -*-
import dataiku
import pandas as pd, numpy as np
from dataiku import pandasutils as pdu
import time

# Read recipe inputs
filesystem = dataiku.Folder("qWeVti46")
filesystem_info = filesystem.get_info()

time.sleep(3000)

# Compute recipe outputs
# TODO: Write here your actual code that computes the outputs
