# -*- coding: utf-8 -*-
import dataikuapi

host= 'http://localhost:11200/'
apiKey = 'TOHkfBiIg2VbPGBVpkqd1Xskf5RKSHSr'
# Read recipe inputs
client = dataikuapi.DSSClient(host, apiKey)
project = client.get_project("EVERYTHING")
imports3_df = project.get_dataset('Imports3')


# Compute recipe outputs
# TODO: Write here your actual code that computes the outputs
# NB: DSS supports several kinds of APIs for reading and writing data. Please see doc.
