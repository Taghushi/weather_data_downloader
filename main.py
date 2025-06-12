from gridmet_downloader import download_Gridmet_inParallel, pull_Gridmet_NC_files
import os
import numpy as np
import requests
from concurrent.futures import ThreadPoolExecutor
import pandas as pd
import glob
import os
import xarray as xr
import shutil

TARGETS = ["tmmx"]
#["tmmx","tmin","rmax","rmin","vs", "bi","erc","pr","srad","vpd","etr","fm100","fm1000","pet","sph","th"]
OUTPUT_PATH = "Joshua_Tree_Gridmet.csv"
START_YEAR = 2024
END_YEAR = 2025

LATITUDE = 33.8734
LONGITUDE = -115.901




def main(output_path, targets, start_year, end_year,lat = 33.8734, lon = -115.901):
    for target in targets:
        download_Gridmet_inParallel(target,start_year,end_year)
        data_dir = os.path.join(os.getcwd(), f"Data/{target}_data")

        path_list = sorted(glob.glob(os.path.join(data_dir, f"{target}_*.nc")))
        
        df = pd.DataFrame()
        for path in path_list:   
            data = xr.open_dataset(path)

            # lat = 33.8734
            # lon = -115.901
            lat_idx = abs(data['lat'] - lat).argmin().item()
            lon_idx = abs(data['lon'] - lon).argmin().item()

            dates = pd.to_datetime(data['day'].values, unit='D')

            var = list(data.data_vars)[0]
            values = data[var][:, lat_idx, lon_idx].values


            
            df1 = pd.DataFrame({
                "date":dates,
                f"{target}": values
            })

            df = pd.concat([df, df1], ignore_index=True)
            data.close()
        df = df.sort_values("date", ascending=True)
        if os.path.exists(output_path):
            old_df = pd.read_csv(output_path)
            old_df["date"] = pd.to_datetime(old_df["date"])
            old_df = old_df.merge(df, on ="date", how ="inner")
            old_df.to_csv(output_path, index=False)
        else:
            df.to_csv(output_path, index=False)
        
        if os.path.exists(data_dir):
            shutil.rmtree(data_dir)
            print(f"Deleted folder: {data_dir}")
        else:
            print(f"Folder does not exist: {data_dir}")



if __name__ == "__main__":
    main(OUTPUT_PATH, TARGETS, START_YEAR, END_YEAR+1, LATITUDE, LONGITUDE)