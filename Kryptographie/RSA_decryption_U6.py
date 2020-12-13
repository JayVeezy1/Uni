# -*- coding: utf-8 -*-
"""
Created on Sun Dec 13 13:26:06 2020

@author: Jakob
"""
# aufgabe a
k = 75
r = 82
y = 89
p = 80
t = 84
o = 79
# exponent = 17
# basis = 629

cypher_k = k**17 % 629
cypher_r = r**17 % 629
cypher_y = y**17 % 629
cypher_p = p**17 % 629
cypher_t = t**17 % 629
cypher_o = o**17 % 629

liste = [cypher_k, cypher_r, cypher_y, cypher_p, cypher_t, cypher_o]
# Ergebnis = [75, 541, 106, 80, 322, 96]
print("Aufgabe a: ", liste)



# aufgabe b
alphabet = {32: ' ', 65: 'a', 66: 'b', 67: 'c',
            68: 'd', 69: 'e', 70: 'f', 71: 'g',
            72: 'h', 73: 'i', 74: 'j', 75: 'k',
            76: 'l', 77: 'm', 78: 'n', 79: 'o',
            80: 'p', 81: 'q', 82: 'r', 83: 's',
            84: 't', 85: 'u', 86: 'v', 87: 'w', 
            88: 'x', 89: 'y', 90: 'z'
            }  
klartext = []
cyphertext = [541, 440, 337, 15, 73, 435, 15, 75, 314, 337, 323, 440, 323, 541]

for letter in cyphertext:
    klar = letter**305 % 629
    klartext.append(klar)
    
for letter in klartext:
    if(letter in alphabet):
        print(letter, alphabet[letter])
    else:
        print(letter, "not found")