# -*- coding: utf-8 -*-
"""
Created on Tue Dec 22 14:26:46 2020

@author: ♫♪ Kevin Fausto ♪♫
"""
print("Ingrese los datos")


space=" "
nombre=input('Ingrese nombre:')
apellido=input('Ingrese apellido:')
locali=input('Ingrese localizacion:')
rango=int(input('Ingrese edad:'))

space=" "
print("Bienvenido:",nombre,apellido,space,"Su edad es:",rango,space,"Se encuentra en:",locali)

if rango>=1 and rango<=11:
    print('Eres un niño!')
    
elif rango>=12 and rango<=17:
    print('Eres un adolescente!')
    
elif rango>=18 and rango<=30:
    print('Eres un joven')
    

else: 
    print('Posiblemente no seas humano....')
