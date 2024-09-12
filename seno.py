def seno(angulo, precisao):
    if angulo > 0 and precisao > 0 :
        cont = 1
        expoente = 1
        resultadofinal = 0
        
    
        for cont in range ( 1, precisao + 1,1):
            resultado = angulo **expoente / fatorial(expoente)

            if cont % 2 != 0:
                resultadofinal = resultado + resultadofinal

            else:
                resultadofinal = resultadofinal - resultado
            
            expoente = expoente + 2
            cont = cont + 1

        
        return resultadofinal

    else:
        resultadofinal = 'erro'
        return resultadofinal



def fatorial(numero):
    if numero >= 0:
        resultado = 1

        for numero in range (numero,0):
            resultado = resultado * numero
            numero = numero - 1

        return resultado

    else:
        resultado = 'erro'
        return resultado

angulo = float(input('Escreva o angulo para calcular seu seno: '))
precisao = int(input('Escreva um numero para calcular a precisão do resultado sendo que quanto maior o numero, maior a precisão: '))
        
print(seno(angulo,precisao))        
