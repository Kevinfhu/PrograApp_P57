# -*- coding: utf-8 -*-
"""
Created on Fri Jan 29 07:47:21 2021

@author: ♫♪ Kevin Fausto ♪♫
"""

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
    if orig =="quit" or orig == "q":
        print("Process Completed , Out of the system!*-ORIG-*")
        break
    dest= input("Destino: ")
    if dest == "quit" or dest== "q":
        print("Process Completed , Out of the system!*-DEST-*")
        break
    url=main_api + urllib.parse.urlencode({"key ":key,"from ":orig,"to ":dest})
    print ("URL: "+(url))
   
    
   
    json_data=requests.get(url).json()
    json_status=json_data["info"]["statuscode"]
    
    if json_status == 0:       
       print("API Status:     "  + str(json_status)+" = A successful route call.\n")
       print("Directions from "  + (orig) +"to"+(dest))
       print("Trip Duration:  "  + (json_data["route"]["formattedTime"]))       
       print("Kilometers:     "  + str("{:.2f}".format((json_data["route"]["distance"])*1.61)))
       print("Fuel Used(Litr): " + str("{:.2f}".format((json_data["route"]["fuelUsed"])*3.78)))       
       print("====================================================================")
       
       for each in json_data["route"]["legs"][0]["maneuvers"]:
           print ((each["narrative"])+"("+str("{:.2f}".format((each["distance"])*1.61)+"km)"))
           
       print("====================================================================")
    elif json_status==402:
       print ("*****************************************************************")
       print ("For status code: "+str(json_status)+"; Invalid user inputs for one or both locations.")
       print ("*****************************************************************\n")
       print("====================================================================")
    else:
       print ("*****************************************************************")
       print("For status code: "+ str(json_status)+";refer to: ")
       print("https://developer.mapquest.com/documentation/directions-api/status-codes")
       print ("*****************************************************************\n")
