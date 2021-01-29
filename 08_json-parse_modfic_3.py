# -*- coding: utf-8 -*-
"""
Created on Wed Jan 27 07:34:10 2021

@author: ♫♪ Kevin Fausto ♪♫
"""

import urllib.parse
import requests
main_api ="https://www.mapquestapi.com/directions/v2/route?"

key="C77qZT3PxHtexb8tK4GLgAkqGqq8gMHS"

while True:
    orig =input("Locacion de inicio: ")
    
    dest= input("Destino:")
    url=main_api + urllib.parse.urlencode({"key":key,"from":orig,"to":dest})
    print ("URL: "+(url))
   
    
   
json_data=requests.get(url).json()
json_status=json_data["info"]["statuscode"]
if json_status == 0:
    print("API Status: " +str(json_status)+" = A successful route call.\n")
