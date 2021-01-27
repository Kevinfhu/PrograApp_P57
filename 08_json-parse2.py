"""
Created on Wed Jan 27 07:34:10 2021

@author: ♫♪ Kevin Fausto ♪♫
"""

import urllib.parse
import requests
main_api ="https://www.mapquestapi.com/directions/v2/route?"
orig="Quito"
dest="Guayaquil"
key="C77qZT3PxHtexb8tK4GLgAkqGqq8gMHS"
url=main_api + urllib.parse.urlencode({"key":key,"from":orig,"to":dest})
json_data = requests.get(url).json()
print(json_data)

print("URL: " + (url))
json_Data=requests.get(url).json()
json_status=json_data["info"]["statuscode"]
if json_status == 0:
    print("API Status: " +str(json_status)+" = A successful route call.\n")
