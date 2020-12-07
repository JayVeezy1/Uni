# -*- coding: utf-8 -*-
"""
Created on Sun Dec  6 16:24:13 2020

@author: Jakob
"""
import pandas as pd
import sklearn
from sklearn.model_selection import train_test_split
from sklearn import tree

def aufgabe_6():
    df = pd.read_csv(r'C:\Users\vanek\Desktop\Wechselwilligkeit_Bestandskunden.csv', delimiter = ';')  
    X = df[['Dauer_durchschnittlich', 'Dauer_kurz', 'Dauer_lang', 
           'Transaktionsvolumen_gering', 'Transaktionsvolumen_hoch', 
           'Transaktionsvolumen_mittel', 'Vertriebsweg_digital', 
           'Reklamierung_vorgefallen']]
    y = df[['Wechsel_ja']]

    # vgl Folie 63 Grundlagen zu Python
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 1)
   
    # Trainieren
    clf = tree.DecisionTreeClassifier(criterion = "entropy")
    clf.fit(X_train, y_train)

    # Prediction der Testdaten
    arr = clf.predict(X_test)
    #print("Vorhersage: ", clf.predict(X_test))
    
    
    # Zusatz - Vergleich:
    print("Vorhersage: ", arr)
    print("Tatsächliche y values: ", y_test.loc[:]['Wechsel_ja'].values)
    predictions = len(X_test.index)
    incorrect_pred = 0
    for i in range(0, predictions):
        if arr[i] != y_test.iloc[i]['Wechsel_ja']:
                incorrect_pred += 1
    print(incorrect_pred, "wrong predictions out of", predictions, "total predictions.")
     
def main():
    aufgabe_6()
    
main()

