import numpy as np

from Due_fasi import due_fasi

def trova_base(A, b): #cerchiamo una base ammissibile nel problema
    
    print("\nCerco una base ammissibile")
    
    indici_base = np.zeros(A.shape[0], dtype=int) #array che conterrà gli indici delle variabili in base relativi a quella che stiamo cercando
    
    for base in range(A.shape[0]): #verifichiamo che sia presente la matrice identica nella matrice A
        
        #creiamo una delle colonne della matrice identica che dovremo trovare in A
        colonna_id = np.zeros(A.shape[0])
        colonna_id[base] = 1
        
        for i in range(A.shape[1]):
            
            if np.array_equal(colonna_id, A[ :, i]): #se la colonna i-esima della matrice è uguale alla colonna della matrice identica...
                indici_base[base] = int(i + 1); #metti l'indice della variabile nell'array delle variabili in base
                break #smetti quindi di cercarla
                
            elif i==A.shape[1]-1: #se non abbiamo trovato la colonna della matrice identica, applichiamo il metodo due fasi
                return due_fasi(A, b)
        
    return indici_base #se abbiamo trovato la matrice identica in A, restituisci gli indici delle relative variabili in base