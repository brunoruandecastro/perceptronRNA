import numpy as np


entradas = np.array ([ [1,1], [1,0], [0,1], [0,0] ])
saidasEsperadas = np.array ([1, -1, -1, -1])
pesos = np.array ( [0.0, 0.0] )
txAprendizagem = 0.1
bias = -1 

def somatorio (entradas):
    
    somatorio = entradas.dot(pesos)
    somatorio = somatorio + bias
    print ("Somatório: %.2f" % (somatorio))
    
    return ativacao(somatorio)

def ativacao (somatorio):
    if somatorio >= 0:
        return +1
    else:
        return -1
    
def treinar():
    quantidadeRodadas = 0 
    erroTotal = None
    
    while (erroTotal != 0):
        erroTotal = 0 
        
        for i in range(len(saidasEsperadas)):
            print ("\nPreposições: " + str(entradas[i]))
            print ("Pesos: " + str(pesos))
            
            sinal = somatorio(np.asarray(entradas[i]))
            print ("Sinal: ", sinal)
            
            erro = abs(saidasEsperadas[i] - sinal)
            
            if (saidasEsperadas[i] != sinal):
                print ("Falhou")
                erroTotal += 1
            else:
                print ("Acertou")
                
            for j in range(len(pesos)):
                if (sinal == -1 and saidasEsperadas[i] == 1):
                    pesos[j] = pesos[j] + (txAprendizagem * erro * entradas[i][j])
                    print ("Peso Atualizado: " +str (pesos[j]))
                        
                if (sinal == 1 and saidasEsperadas[i] == -1):
                    pesos[j] = pesos[j] - (txAprendizagem * erro * entradas[i][j])
                    print ("Peso Atualizado: " +str (pesos[j]))
                        
                        
        quantidadeRodadas +=1
        print ("Total de rodadas: %s" % (quantidadeRodadas))
        print ("Total de erros encontrados na rodada: %s \n\n" % (str(erroTotal)))
        
                        
treinar()
print ("Rede treinada")


preposicao = np.array ([1,0])
print ("Preposição: ", preposicao)

teste = somatorio(preposicao)
if teste == 1:
    print ("Verdadeiro")
else:
    print ("Falso")