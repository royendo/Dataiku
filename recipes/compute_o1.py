# -*- coding: utf-8 -*-
import dataikuapi

host= 'http://localhost:11200/'
apiKey = 'TOHkfBiIg2VbPGBVpkqd1Xskf5RKSaaaHSra'
print(apiKey)
# Read recipe inputs
client = dataikuapi.DSSClient(host, apiKey)
project = client.get_project("EVERYTHING")
Oracle = project.get_dataset('ToOracle')


# Compute recipe outputs
# TODO: Write here your actual code that computes the outputs
# NB: DSS supports several kinds of APIs for reading and writing data. Please see doc.
