import numpy as np

#dato il vettore ccr restituisce l'indice della var entrante (Bland)
def var_entrante(ccr, min_max):
    
    for i in range(ccr.shape[0]): #scorri il vettore dei ccr per restituire l'indice del primo elemento negativo (Bland)
        
        if not min_max: #se si tratta di un problema di minimo...
            if ccr[i]<0:
                return i + 1 #restituisci l'indice della prima variabile con ccr negativo
            
        else: #se si tratta di un problema di massimo...
            if ccr[i]>0:
                return i + 1 #restituisci l'indice della prima variabile con ccr positivo

            
#dato il vettore b_ e la colonna A_h restituisce l'indice della var uscente (Bland)
def var_uscente(A_h, b_, var_base):
    
    var_uscente = None #impostiamo di default l'indice per la variabile uscente
    
    for i in range(A_h.shape[0]): #scorri la colonna A_h per cercare un valore negativo nella colonna h del tableau (Bland)
        
        if A_h[i]>0: #se abbiamo trovato un coefficiente strettamente positivo...
            
            rapporto_i = b_[i]/A_h[i] #metti in rapporto_i il rapporto tra termine noto e coeff della colonna h del tableau
            
            if var_uscente is None: #se ancora non abbiamo scelto un indice per una var uscente...
                var_uscente = var_base[i] #aggiorna l'indice della var uscente
                rapporto = rapporto_i #mettiamo il valore del rapporto tra il termine noto e l'elemento della colonna A_h in rapporto
                
            elif rapporto_i < rapporto: #se abbiamo trovato un rapporto minore di quello precedente...
                var_uscente = var_base[i] #aggiorna l'indice della var uscente
                rapporto = rapporto_i #aggiorna il rapporto
                
            elif (rapporto_i == rapporto) & (var_base[i] < var_uscente): #se il rapporto è identico, ma l'indice della variabile è minore...
                var_uscente = var_base[i] #aggiorna l'indice della var uscente
                
    return var_uscente
  
    
#sostituisci nel vettore delle variabili di base l'indice della var uscente con l'indice della var entrante
def sostituisci_var(var_base, t, h):
    
    for i in range(var_base.shape[0]): #cerca all'interno dell'array degli indici delle var in base l'indice della var uscente
        if var_base[i] == t:
            var_base[i] = h #una volta trovato, sostituiscilo con l'indice della var entrante  