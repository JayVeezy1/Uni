# -*- coding: utf-8 -*-
"""
Created on Sun Dec  6 14:52:18 2020

@author: Jakob
"""
import pandas as pd

# wofuer wird das r gebraucht?
def aufgabe_5():
    df = pd.read_csv(r'C:\Users\vanek\Desktop\Mitarbeiterdaten.csv',
                     delimiter = ";",
                     index_col = "PerNr"
                     )
    # 1. check ob dataframe existiert
    print(df, "\n")
    
    # 2. waehle bestimmte PerNr (index) 
    print(df[df.index == 124532], "\n")
    
    # 3. waehle nur Geb spalte
    print(df.Geb, "\n")
    
    # 4. waehle Jahresgehalt von bestimmtem Namen 
    # iloc fuer row position
    # print(df.iloc[3]['Jahresgehalt'], "\n")
    # loc fuer index-label - aber wenn index unbekannt?
    # print(df.loc[139823]['Jahresgehalt'], "\n")
    # loc kombiniert mit condition returnt neuen gefilterten df, aber nur zellen-value gewollt!
    # print(df.loc[df.Name == 'Hofstadter', ['Jahresgehalt']], "\n")
    # ueber values auf (einzigen) wert des gefilterten df zugreifen
    print(df.loc[df.Name == 'Hofstadter', ['Jahresgehalt']].values[0][0], "\n")
    
    # 5. Addiere zwei Gehaelter  
    hofstadter_gehalt = df.loc[df.Name == 'Hofstadter', ['Jahresgehalt']].values[0][0]
    cooper_gehalt = df.loc[df.Name == 'Cooper', ['Jahresgehalt']].values[0][0]
    print(hofstadter_gehalt + cooper_gehalt)    
    
    
def main():
    aufgabe_5()
    
main()
