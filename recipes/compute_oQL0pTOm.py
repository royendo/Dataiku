import dataiku

client = dataiku.api_client()
project = client.get_project('EVERYTHING')

# Read recipe inputs
tests = dataiku.get_managed_folder("iV6c3jWU")
tests_info = tests.get_info()


# Write recipe outputs
folder = dataiku.get_managed_folder("oQL0pTOm")
folder_info = folder.get_info()


# target_folder will now contain a copy of all files that were in source_folder
future = tests.copy_to(folder)
future.wait_for_result()