# -*- coding: utf-8 -*-
"""
Created on Tue Jan  5 15:28:01 2021

@author: ♫♪ Kevin Fausto ♪♫
"""


while True:
    x=input('Enter a number to count to: ')
    if x == "q" or x=="quit":
        break
    x=int(x)
    y=1
    while True:
        print(y)
        y=y+1
        if y>x:
            break