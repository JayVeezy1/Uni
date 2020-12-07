# -*- coding: utf-8 -*-
"""
Created on Sat Dec  5 16:35:27 2020

@author: Jakob
"""
import math

def aufgabe_1a():
    vorname = input ("Vorname?")
    nachname = input("Nachname?")
    print("Hello,", vorname, nachname)

def aufgabe_1b():
    text = "blabla"
    boo = True
    my_int = 13
    my_float = 1.3
    print(" text:", "\t", type(text), "\n", 
          "boo:", "\t", type(boo), "\n", 
          "my_int:", "\t", type(my_int), "\n",
          "my_float:", "\t", type(my_float), "\n"
          )
    
def aufgabe_1c():
    my_liste = ["a", False, 1, 2.0]
    my_tupel = (15, 30, 45, 60)
    my_dict = {
        "first" : "abc",
        "second" : 22,
        "third" : 33,
        "whatever" : "whenever"
    }
    print(my_liste[0], my_tupel[1], my_dict["second"])

def aufgabe_1d():
    K_0 = 1000
    r = 0.1
    zins = 1 + r
    n = 5
    
    K_n = K_0 * math.pow(zins, n)
    print(round(K_n, 2))
    
def aufgabe_1e():
    # Quadratische Gleichung: a*x^2 + b*x + c
    a = 2
    b = 2
    c = -12
    
    # Mitternachtsformel fuer NST
    x_1 = (-b + math.sqrt(math.pow(b, 2) - 4 * a * c)) / (2 * a)
    x_2 = (-b - math.sqrt(math.pow(b, 2) - 4 * a * c)) / (2 * a)
    ergebnis = [round(x_1, 2), round(x_2, 2)]
    print(ergebnis)
    # nichts zu runden???
    
def main():
    # aufgabe_1a()
    # aufgabe_1b()
    # aufgabe_1c()
    # aufgabe_1d()
    aufgabe_1e()
    
main()
