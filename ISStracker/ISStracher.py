#!/usr/bin/env python3
"""This program aquires ISS location data and overlays it on a map using Folium"""

#JSON format for ISS_API
"""{
    "message": "success",
    "iss_position": {
        "longitude": "128.5297",
        "latitude": "-5.7925"
    },
    "timestamp": 1707343260
}"""

# notice we no longer need to import urllib.request or json
import requests
#import urllib.requests
#import json

# import folium library to plot map overlay and ISS/User markers
import folium

# APIs to access data on ISS and User location (if time permiting)
ISS_API = "http://api.open-notify.org/iss-now.json"

# this function grabs the ISS's location data (with timestamp)
def returnISSdata():
    ## Get ISS data using open API
    ISSdata = requests.get(ISS_API)
    ## Convert API data to JSON 
    ISSdata_JSON = ISSdata.json()
    return ISSdata_JSON

def main():
    """runtime function"""
    ## Use ISStracker API to get ISS location information
    ISS_data = returnISSdata()
    ## Test that can aquire data using API
    print(ISS_data)
    ## Parce returned API data into a list or variables
    

    ## create map 
    m = folium.Map(location=(45.5236, -122.6750))
    ## save as .html file 
    m.save("index.html")
    ## test opening file in web browser
    firefox index.html


# call our main function
if __name__ == "__main__":
    main()
