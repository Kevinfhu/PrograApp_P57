# -*- coding: utf-8 -*-
"""
Created on Tue Jan 19 14:48:27 2021

@author: ♫♪ Kevin Fausto ♪♫
"""
file=open('devices.txt','a')
while True:
    
    newItem=input('Input Name of new Device: ')
    if newItem== 'exit':
        print('ALL DONE!')
        break
    file.write(newItem + "\n")
    file.close()
 
