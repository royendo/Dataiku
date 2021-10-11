# -*- coding: utf-8 -*-
import dataiku

remote = dataiku.set_remote_dss("http://localhost:11200/", "TOHkfBiIg2VbPGBVpkqd1Xskf5RKSHSr")
print(remote)
connection = dataiku.get_connection("ToOracle")

'''
host= 'http://localhost:11200/'
apiKey = 'TOHkfBiIg2VbPGBVpkqd1Xskf5RKSHSr'
print(apiKey)
# Read recipe inputs
client = dataikuapi.DSSClient(host, apiKey)
project = client.get_project("EVERYTHING")
Oracle = project.get_dataset('ToOracle')

connection = dataikuapi.dss.admin.DSSConnection(client, 'Oracle')
print(connection.get_info())
# Compute recipe outputs
# TODO: Write here your actual code that computes the outputs
# NB: DSS supports several kinds of APIs for reading and writing data. Please see doc.
'''

