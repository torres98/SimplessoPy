import numpy as np
from Simplex import simplex

def due_fasi(A, b):
    
    print("\nApplico il metodo due fasi")
    rows_A = A.shape[0]
    columns_A = A.shape[1]
    
    #generiamo a partire dal problema di partenza il problema 'artificiale'
    base = np.identity(rows_A) #genera la matrice identica per le variabili artificiali (in base al num di righe)
    artificial_A = np.concatenate((A, base), axis=1) #genera la nuova matrice dei coefficienti concatenando A e la matrice identica
    
    #generiamo il vettore dei coefficienti di costo della nuova f obiettivo
    artificial_c = np.zeros(rows_A + columns_A)
    artificial_c[columns_A:] = 1
    
    var_base = np.arange(columns_A + 1, columns_A + rows_A + 1) #specifichiamo come variabili di base gli indici delle var. artificiali
    
    ottimo = simplex(artificial_A, b, artificial_c, base, var_base, False) #risolvi tramite il simplesso il problema di minimo appena generato
    
    print("\nOTTIMO: ", ottimo)
    
    if ottimo > 0: #non esiste una base ammissibile, quindi ritorna None
        return None
    
    elif ottimo==0: 
        
        if (var_base > columns_A).any(): #se c'è almeno un indice di una variabile artificiale nelle var di base...
            base_degenere(A, base, var_base) #allora applica l'algoritmo per la base degenere
        
        return var_base
        
def base_degenere(A, base, var_base):
    
    columns_A = A.shape[1]
    rows_A = A.shape[0]
    
    F = np.zeros((rows_A, columns_A - rows_A)) #crea la matrice di partenza per la matrice F

    var_fuori = np.zeros((A.shape[0])) #crea l'array di partenza per gli indici delle variabili fuori base
    
    column = 0
        
    for i in range(columns_A): #per ogni colonna della matrice A
        if not (var_base == i + 1).any(): #se l'indice che stiamo valutando non è in base...
            var_fuori[column] = i + 1 #metti nell'array degli indici delle var fuori base l'indice della colonna corrente
            F[:, column] = A [:, i] #metti in F la colonna corrispondente di A
            column += 1 #incrementiamo l'indice della colonna di F da inserire
            
    while (var_base > columns_A).any(): #finchè ci sono in base variabili artificiali...
            
        A_ = np.matmul(np.linalg.inv(base), F) #calcola la matrice A_ del tableau
        
        for i in range(var_base.shape[0]): #scorriamo l'array degli indici delle var in base...
            if var_base[i] > columns_A: #se troviamo un indice di una var artificiale...
                usc = i #memorizza in usc l'indice posizionale della var di base y all'interno del vettore delle var di base
                y = var_base[i] #memorizza in y l'indice della variabile artificiale y
                break
                
        if (A_[usc, :] != 0).any(): #se è presente almeno un valore non nullo nella riga della var artificiale in A_h...
            
            h = np.where(A_[usc, :] !=0)[0][0] #cerca l'indice di uno degli elementi non nulli
            h = var_fuori[h] #troviamo l'indice della variabile fuori base a cui si riferisce la colonna dell'elemento non nullo
            base[:, usc] = A[:, h - 1] #aggiorna la matrice di base sostituendo la colonna della var uscente y con la colonna della var entrante h
            
            var_fuori[h - 1] = usc + 1 #aggiorna l'array delle variabili fuori base, inserendo l'indice della var artificiale y
            var_base[usc] = h #aggiorna l'array delle variabili in base, inserendo l'indice della var h
            
            F[:, h - 1] = A[:, usc] #aggiorna la matrice F sostituendo la colonna della var entrante h con la colonna della var uscente y
            base[:, usc] = A[:, h - 1] #aggiorna la matrice B sostituendo la colonna della var uscente y con la colonna della var entrante h
            
        else: #altrimenti, se la riga risulta linearmente indipendente...
            
            A = np.delete(A, usc, 0) #elimino la riga della var artificiale y
            A = np.delete(A, y - 1, 1) #elimino la colonna della var artificiale y
            
            var_base = np.delete(var_base, np.where(var_base == y)[0][0], 0) #elimino dalle variabili in base la var y
            
            F = np.delete(F, usc, 0) #elimino anche da F la riga della var artificiale y
            base = np.delete(base, usc, 0) #elimino anche da B la riga della var artificiale y
            base = np.delete(base, usc, 1) #elimino anche da B la colonna della var artificiale y
            
                
        