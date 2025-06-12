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

    - This is a py file that pulls nc files from Gridmet, which is a public government weather website
    - nc files are an interesting data object that each contain a year's worth of weather data for 
      every latitude and longitude grid point (4 km by 4 km) in the United States, so you can get data
      for any location in the US with my code.
    - My code downloads all nc files for the years specified and for variables specified by user. It then
      selects the user input lat and lon, extracts the data, and reformats it into a csv. It deletes the
      nc files to prevent the user from wasting disk on their local computer.
    - Now you have data in a readable format that is compatbile with many analysis and machine learning libraries!
