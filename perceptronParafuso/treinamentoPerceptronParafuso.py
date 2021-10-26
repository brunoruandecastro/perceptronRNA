import numpy as np


entradas = np.array ([ [4,3],[1,1],[3,1],[2,3],[5,3],[3,2] ])
saidasEsperadas = np.array ([1,-1,-1,1,1,1])
pesos = np.array([0.0,0.0])
txAprendizagem = 0.01
bias = -1

def somatorio(entradas):
    somatorio = entradas.dot(pesos)
    somatorio = somatorio + bias
    print ("Somatório", somatorio)
    
    return ativacao(somatorio)

def ativacao(somatorio):
    if (somatorio >=0):
        return 1
    else:
        return -1
    
def treinar():
    quantidadeRodadas= 0 
    erroTotal = None
    
    while (erroTotal != 0):
        erroTotal = 0
        
        for i in range (len(saidasEsperadas)):
            print("\nParafuso: " + str(entradas[i]))
            print ("Pesos: " + str(pesos))
            
            sinal = somatorio(np.asarray(entradas[i]))
            erro = abs(saidasEsperadas[i] - sinal)
            
            if (saidasEsperadas[i] != sinal):
                print("Errado")
                erroTotal += 1
            else:
                print ("Certo")
                
            for j in range(len(pesos)):
                if (sinal == -1 and saidasEsperadas[i] == 1):
                    pesos[j] = pesos[j] + (txAprendizagem *erro* entradas[i][j])
                    print ("Peso Atualizado: " + str(pesos[j]))
                
                
                if (sinal == 1 and saidasEsperadas[i] == -1):
                    pesos[j] = pesos[j] - (txAprendizagem *erro* entradas[i][j])
                    print ("Peso Atualizado: " + str(pesos[j]))
                    
            
            quantidadeRodadas +=1
            print("Total de erros da rodada: %s" %(str(erroTotal)))
            print("Total de rodadas: %s \n\n" % (str(quantidadeRodadas)))
            

treinar()
print ("Rede Treinada")

teste = somatorio(np.array([1,2]))

if teste == 1:
    print("Classe A")
else:
    print("Classe B")
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
