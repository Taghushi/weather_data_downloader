# weather_data_downloader
Use this code for downloading daily Government Weather Data. It is high quality data that can be used for data analysis or machine learning.

- main.py
    - User must go to top of the file and set the input arguments:
        - OUTPUT_PATH: The name of output csv where data is downloaded.
        - START_YEAR: Starting year of data you want (earliest year is 1979)
        - END_YEAR: Last year of data you want (goes until present which is 2025 right now)
        - Input the last year of data you want (goes until present which is 2025 right now)
        - LATITUDE: The latitude of your target location (I automatically set it to Joshua Tree)
        - LONGITUDE: The longitude of your target location (I automatically set it to Joshua Tree)
- gridmet_downloader
    - This contains functions that I created that are needed to run main.py.
- Joshua_Tree_Gridmet.csv
    - This is an exmaple of what the data will look like after running the code.
    - I just used tmmx and tmmn and years 2024 to 2025 for this example.

- This is a py file that pulls nc files from Gridmet, which is a public government weather website
- nc files are an interesting data object that each contain a year's worth of weather data for 
  every latitude and longitude grid point (4 km by 4 km) in the United States, so you can get data
  for any location in the US with my code.
- My code downloads all nc files for the years specified and for variables specified by user. It then
  selects the user input lat and lon, extracts the data, and reformats it into a csv. It deletes the
  nc files to prevent the user from wasting disk on their local computer.
- Now you have data in a readable format that is compatbile with many analysis and machine learning libraries!

- Gridmet Variables:
    * sph: (Near-Surface Specific Humidity)
    * vpd: (Mean Vapor Pressure Deficit)
    * pr: (Precipitation)
    * rmin: (Minimum Near-Surface Relative Humidity)
    * rmax: (Maximum Near-Surface Relative Humidity)
    * srad: (Surface Downwelling Solar Radiation)
    * tmmn: (Minimum Near-Surface Air Temperature)
    * tmmx: (Maximum Near-Surface Air Temperature)
    * vs: (Wind speed at 10 m)
    * th: (Wind direction at 10 m)
    * pdsi: (Palmer Drought Severity Index)
    * pet: (Reference grass evaportranspiration)
    * etr: (Reference alfalfa evaportranspiration)
    * erc: (model-G)
    * bi: (model-G)
    * fm100: (100-hour dead fuel moisture)
    * fm1000: (1000-hour dead fuel moisture)
