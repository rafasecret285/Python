def fatorial(numero):
    if numero >= 0:
        resultado = 1
        começo=numero

        for numero in range(começo,1,-1):
            resultado = resultado * numero
            numero = numero - 1

        return resultado
    else:
        print('O número precisa ser positivo')
        return -1
    

numero = int(input('Digite um número inteiro positivo'))
print(fatorial(numero))


    
