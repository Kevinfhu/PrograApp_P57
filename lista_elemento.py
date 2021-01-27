# -*- coding: utf-8 -*-
"""
Created on Tue Jan 19 14:19:02 2021

@author: ♫♪ Kevin Fausto ♪♫
"""
lista=[]
file=open('devices.txt')
for a in file:
    a=a.strip()
    lista.append(a)
    print(a)
    file.close
    print (lista)
