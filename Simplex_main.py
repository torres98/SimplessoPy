import numpy as np

from Simplex import simplex
from Trova_base import trova_base

def simplex_main(A, b, c, min_max): #algoritmo che cerca una base ammissibile di partenza e applica successivamente l'algoritmo del simplesso
    
    ottimo = None
    var_base = trova_base(A, b) #troviamo una base ammissibile per il problema
    
    if var_base is None: #se non esiste una base ammissibile, allora stampa un errore
        print ("Non esiste una base ammissibile, il problema e' vuoto!\n")
        
    else: #altrimenti applica l'algoritmo del simplesso
        print("\nRisolvo il problema con la base di partenza trovata")
        base = A[:, var_base-1] #estrai le colonne delle var in base dalla matrice A e mettile nella matrice base
        ottimo = simplex(A, b, c, base, var_base, min_max)
            
    return ottimo