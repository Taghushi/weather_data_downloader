# weather_data_downloader
This is my pipeline for downloading Government Weather Data, and using it to train a
machine learning model to predict daily weather variables. I personally use it for 
informed camping decisions!

- 1) Gridmet_DataDownload_and_Processing.py
    - User must go to the bottom of the file and input the following in the main function:
            - Input the name of their output path csv
            - Input the list of gridmet variables you want (you can see a list of variables 
            at the bottom of this READ_ME)
            - Input the starting year of data you want (earliest year is 1979)
            - Input the last year of data you want (goes until present which is 2025 right now)
            - Input the latitude of your target location (I automatically set it to Joshua Tree)
            - Input the longitude of your target location (I automatically set it to Joshua Tree)

    - This is a py file that pulls nc files from Gridmet, which is a public government weather website
    - nc files are an interesting data object that each contain a year's worth of weather data for 
      every latitude and longitude grid point (4 km by 4 km) in the United States, so you can get data
      for any location in the US with my code.
    - My code downloads all nc files for the years specified and for variables specified by user. It then
      selects the user input lat and lon, extracts the data, and reformats it into a csv. It deletes the
      nc files to prevent the user from wasting disk on their local computer.
    - Now you have data in a readable format that is compatbile with many analysis and machine learning libraries!
