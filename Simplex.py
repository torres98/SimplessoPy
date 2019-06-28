import numpy as np

from Operazioni_var import var_entrante, var_uscente, sostituisci_var

def simplex(A, b, c, base, var_base, min_max):
    
    illimitato = False
    ottimo = False
    
    iteration = 1
        
    while (not ottimo) & (not illimitato):
    
            print("\n\\\Iterazione ", iteration, "///")
        
            inverted_base = np.linalg.inv(base) #calcolo l'inversa della base
        
            c_b = c[var_base - 1] #preleviamo i coefficienti di costo delle variabili in base
            
            u_t = np.matmul(np.transpose(c_b), inverted_base) #calcolo il vettore trasposto di u (u = c_b * B^-1)

            ccr = np.subtract(np.transpose(c), np.matmul(u_t, A)) #calcolo i coefficienti di costo ridotto (ccr = c - u * A)
         
            print("\nCCR:")
            print(ccr)
            
            print("\nBASE:")
            print(base)
            
            print("\nC_b:")
            print(c_b)
            
            print("\nVar in base:")
            print(var_base)
            
            if not min_max: #se si tratta di un problema di minimo...
                
                if not_neg(ccr): #se i ccr sono tutti non negativi allora siamo in condizioni di ottimalità
                    ottimo = True
                    
            else: #se si tratta di un problema di massimo...
                    
                if not_pos(ccr): #se i ccr sono tutti non positivi allora siamo in condizioni di ottimalità
                    ottimo = True
                
            if not ottimo:
                
                h = var_entrante(ccr, min_max) #var_entrante restituisce l'indice della variabile da far entrare (tramite Bland)
                b_ = np.matmul(inverted_base, b)
                A_h = np.matmul(inverted_base, A[:, h-1])
            
                if not_pos(A_h):
                    illimitato = True
                
                else:
                    t = var_uscente(A_h, b_, var_base) #var_uscente restituisce l'indice della variabile da far uscire (tramite Bland)
                    
                    usc = np.where(var_base == t)[0][0]
                    base[:, usc] = A[:, h - 1] #aggiorna la matrice di base sostituendo la colonna della var t con la colonna della var h
                    
                    sostituisci_var(var_base, t, h) #modifica l'indice delle variabili in base di conseguenza
    
            iteration += 1
        
    if illimitato:
        print("Il problema e' illimitato!\n")
        return None
    
    else:
        
        x_b = np.matmul(inverted_base, b)
        
        print("\nOTTIMO TROVATO\n\nValori di X_B: ")
        print(x_b)
        
        soluzione = np.matmul(np.transpose(c_b), x_b)
        print("\nValore Ottimo: ", soluzione)
    
        return soluzione
    
def not_neg(array): #restituisce True se l'array è formato solo da elementi non negativi, False altrimenti
    
    return not (array < 0).any()


def not_pos(array): #restituisce True se l'array è formato solo da elementi non positivi, False altrimenti
    
    return not((array > 0).any())