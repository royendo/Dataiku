# -*- coding: utf-8 -*-
import dataikuap
import dataikuapi.dss.admin

host= 'http://localhost:11200/'
apiKey = ''
print(apiKey)
# Read recipe inputs
client = dataikuapi.DSSClient(host, apiKey)
project = client.get_project("EVERYTHING")
Oracle = project.get_dataset('ToOracle')

connection = dataikuapi.dss.admin.DSSConnection(client, 'Oracle')

# Compute recipe outputs
# TODO: Write here your actual code that computes the outputs
# NB: DSS supports several kinds of APIs for reading and writing data. Please see doc.
