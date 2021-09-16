# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
# %pylab inline

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
#import packages

import dataiku
from dataiku import pandasutils as pdu
import pandas as pd
import datetime
import os

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
input_folder_name='DEVELOPMENT' #specify from which project folder the projects need to be exported
output_folder_name='ACCEPTANCE' # specify output project folder

#DEVELOPMENT, ACCEPTANCE, TEST, PRODUCTION

def get_folder(folder_name, root_folder):
"""
Get the dataiku folder by folder name.
folder_name: the folder to search for.
root_folder: the root_folder of the dataiku client
Returns dataiku project folder
"""
project_folder_names=[x.name for x in root_folder.list_child_folders()]
project_folder_ids=[x.id for x in root_folder.list_child_folders()]
folder_index=project_folder_names.index(folder_name)
folder_id=project_folder_ids[folder_index]
project_folder=client.get_project_folder(folder_id)
return project_folder

def get_metadata():
client = dataiku.api_client()
root=client.get_root_project_folder()
time = datetime.datetime.now()
user=client.get_auth_info()["authIdentifier"]
return client, root, time, user

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
#get dataiku metadata
client, root, time, current_user = get_metadata()

#get input and output folder
input_project_folder=get_folder(input_folder_name,root)
output_project_folder=get_folder(output_folder_name,root)

#get projects in input folder
project_key_list = ["DEV_INVESTMENTMONITORING"]

#get prefixes and connections
prefix_dict={'DEVELOPMENT':'DEV_','TEST':'TST_', 'ACCEPTANCE':'ACC_','PRODUCTION':'PRD_'}
permission_group='DEV_ILI' if output_folder_name=='DEVELOPMENT' else 'USR_ILI'
in_prefix=prefix_dict[input_folder_name]
out_prefix=prefix_dict[output_folder_name]

EMI_pfx={'DEVELOPMENT':'ACC_','TEST':'ACC_', 'ACCEPTANCE':'PRD_','PRODUCTION':'PRD_'}
EMI_pfx_in=EMI_pfx[input_folder_name]
EMI_pfx_out=EMI_pfx[output_folder_name]

connections_dict={ 'connections' :[{ 'source' : EMI_pfx_in+'SQL_EMI' , 'target' : EMI_pfx_out+ 'SQL_EMI' }]}

for project_key in project_key_list:
project = client.get_project(project_key)
out_prj_key=project_key.replace(in_prefix,out_prefix)
dupl_dict=project.duplicate(out_prj_key, prj_name,\
target_project_folder=output_project_folder,remapping=connections_dict)