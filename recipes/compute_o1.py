# -*- coding: utf-8 -*-
import dataikuapi

host= 'http://localhost:11200/'
apiKey = 'TOHkfBiIg2VbPGBVpkqd1Xskf5RKSHSr'
# Read recipe inputs
client = dataikuapi.DSSClient(host, apiKey)
imports3_df = DSSDataset(client, 'EVERYTHING','Imports3')


# Compute recipe outputs
# TODO: Write here your actual code that computes the outputs
# NB: DSS supports several kinds of APIs for reading and writing data. Please see doc.
