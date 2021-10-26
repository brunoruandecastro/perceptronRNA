entradas = [0, 0]
pesos = [0.6, 0.6]
bias = -1


def somatorio(entradas, pesos):
    somatorio = 0
    
    for i in range(2): #ler os valores
        somatorio += entradas [i] * pesos [i]
        
        print ("Parcial somatório: ", somatorio)
        
    
    somatorio = somatorio + bias
    print ("Final somatório: %.2f" % (somatorio))
    
    return ativacao(somatorio)

def ativacao (somatorio):
    if (somatorio >= 0):
        print ("Verdadeiro")
        return +1
    else:
        print ("Falso")
        return -1
    
somatorio = somatorio(entradas, pesos)







