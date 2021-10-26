import numpy as np

entradas = np.array ([ [1, 1], [1, 0], [0, 1], [0, 0] ])
pesos = np.array( [0.6, 0.6] )
bias = -1

def somatorio(entradas):
    
    somatorio = entradas.dot(pesos)
        
    somatorio = somatorio + bias
    print ("Somatório: %.2f" % (somatorio))
    
    return ativacao(somatorio)

def ativacao(somatorio):
    if (somatorio >= 0):
        print("Verdadeiro")
        return + 1
    else:
        print ("Falso")
        return -1
    
for entrada in entradas:
    print(entrada)
    somatorio(entrada)
    print("\n")
    
    
    
    
    
    
    