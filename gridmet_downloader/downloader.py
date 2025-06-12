import os
import numpy as np
import requests
from concurrent.futures import ThreadPoolExecutor
#import pandas as pd
#import glob
import os
import xarray as xr
#import shutil

def pull_Gridmet_NC_files(target_var, year):    
    base_url = "https://www.northwestknowledge.net/metdata/data/"
    #target_var = "bi"
    year = str(year)

    local_destination = f"Data/{target_var}_data"

    os.makedirs(local_destination, exist_ok=True)

    
    #for i in years:
    #year = str(i)
    file_name = f"{target_var}_{year}.nc"
    url = f"{base_url}{file_name}"
    output_path = os.path.join(local_destination, file_name)
    if os.path.exists(output_path):
        print(f"File {file_name} already exists, skipping.")
        return True
    
    response = requests.get(url)
    response.raise_for_status()
    with open(output_path, "wb") as f:
        for chunk in response.iter_content(chunk_size = 8192):
            if chunk:
                f.write(chunk)
    return True

        
    
def download_Gridmet_inParallel(target_var, start_year, end_year):
    years = np.arange(start_year,end_year)
    # for i in years:
    #     year = str(i)
    inputs = []
    for year in years:
        tup = (target_var,year)
        inputs.append(tup)
    with ThreadPoolExecutor(max_workers = 4) as worker:
        futures = []
        for input in inputs:
            future = worker.submit(pull_Gridmet_NC_files, input[0],input[1])
            futures.append(future)
        for future in futures:
            future.result()