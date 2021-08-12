import dataiku
import pandas as pd, numpy as np
from dataiku import pandasutils as pdu
from netCDF4 import Dataset, num2date
import xarray as xr
import os, tempfile
from dataikuutils import copy_file_to_temp_folder


with tempfile.TemporaryDirectory() as temp_dir_name:
    selected_partition_year = dataiku.dku_flow_variables["DKU_DST_year"]

    # Read recipe inputs
    cds = dataiku.Folder("S3")
    paths = cds.list_paths_in_partition()
    folder = cds.get_partition_folder(selected_partition_year)

    copy_file_to_temp_folder(cds, os.path.join(folder, "era5.nc"), temp_dir_name)

    #for path in paths:
    #with cds.get_download_stream(os.path.join(folder, "era5.nc")) as f:
    #dataset = Dataset("temp.nc", memory=f.read(), diskless=True)
    #print("dataset file format", dataset.file_format)
    print("dir", str(temp_dir_name+os.path.join(folder, "era5.nc")))
    ds = xr.load_dataset(str(temp_dir_name+os.path.join(folder, "era5.nc")), chunks='auto')
    cds_parsed_df = ds.to_dataframe()
    cds_parsed_df.reset_index(inplace=True)  


    # Write recipe outputs
    cds_parsed = dataiku.Dataset("25088")
    cds_parsed.write_with_schema(cds_parsed_df)