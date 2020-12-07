# -*- coding: utf-8 -*-
"""
Created on Sun Dec  6 14:42:32 2020

@author: Jakob
"""

def aufgabe_3a():
    liste = []
    for i in range(0, 100):
        if (i % 7 == 0):
            liste.append(i)
        i += i
    return(liste)

def main():
    print(aufgabe_3a())
    
main()