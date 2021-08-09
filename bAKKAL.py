# -*- coding: utf-8 -*-
"""
Created on Wed Dec 23 14:16:30 2020

@author: Hale Nur
"""
#Bakkal

#Ürün Listesi

ürünList = {
    "ekmek":1.5,
    "pirinç":10,
    "süt":6,
    "Yumurta":15
    }

#ürün ekle 

addProduct = input("Ürün gir:")
addPrice = float(input("Fiyat Gir :"))
add = ürünList.update({addProduct:addPrice})
print("Güncel Liste",ürünList)

#Sepet

print(ürünList)
alınacaklar=input("ürün girin:")

