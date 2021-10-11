# -*- coding: utf-8 -*-
import dataikuapi

host= 'http://localhost:11200/'
apiKey = 
# Read recipe inputs
imports3 = dataikuapi.DSSClient(host, apiKey)
imports3_df = imports3.get_dataframe()


# Compute recipe outputs
# TODO: Write here your actual code that computes the outputs
# NB: DSS supports several kinds of APIs for reading and writing data. Please see doc.
