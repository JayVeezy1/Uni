# -*- coding: utf-8 -*-
"""
Created on Sun Dec  6 14:28:52 2020

@author: Jakob
"""
import math

def aufgabe_2a():
    # Quadratische Gleichung: a*x^2 + b*x + c
    # Fall 1: x_1: 0.62 x_2: -1.62
    #a = 2
    #b = 2
    #c = -2
    # Fall 2: x1 == x2 : 4.5
    #a = 4
    #b = -36
    #c = 81
    # Fall 3
    a = 2
    b = 1
    c = 2
    
    try:
        x_1 = (-b + math.sqrt(math.pow(b, 2) - 4 * a * c)) / (2 * a)
        x_2 = (-b - math.sqrt(math.pow(b, 2) - 4 * a * c)) / (2 * a)
        ergebnis = [round(x_1, 2), round(x_2, 2)]
        if (x_1 == x_2):
            print("x1 == x2 :", round(x_1, 2))
        else:
            print("x_1:", round(x_1, 2), "x_2:", round(x_2, 2))
    except ValueError:
            print("Kein Ergebnis verfügbar wegen: math domain error")
    except:
            print("Kein Ergebnis verfügbar wegen: sonstiger Fehler")
    
def main():
    aufgabe_2a()
    
main()