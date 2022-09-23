import dataiku

client = dataiku.api_client()
project = client.get_project('EVERYTHING')

# Read recipe inputs
tests = project.get_managed_folder("iV6c3jWU")



# Write recipe outputs
folder = project.get_managed_folder("oQL0pTOm")


# target_folder will now contain a copy of all files that were in source_folder
future = tests.copy_to(folder)
future.wait_for_result()