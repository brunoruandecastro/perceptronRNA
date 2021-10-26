import numpy as np


entradas = np.array ([[4,3],[1,1],[3,1],[2,3],[5,3],[3,2]])
pesos = np.array([0.21, 0.22])
bias = -1

def somatorio (entradas):
    somatorio = entradas.dot(pesos)
    somatorio = somatorio + bias
    print ("Somatório: %.2f" % (somatorio))
    
    return ativacao(somatorio)

def ativacao (somatorio):
    if (somatorio >= 0):
        print ("Parafuso da classe A")
    else:
        print ("Parafuso da classe B")
        
        
for parafuso in entradas:
    
    print("Parafuso de tamanho: ", parafuso)
    s = somatorio(parafuso)
    print("")