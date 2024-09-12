def somaFatorial(numero):
    if numero > 0:
        resultado = 0

        while numero > 0:
            resultado = resultado + numero
            numero = numero - 1
        return resultado

    elif numero == 0:
        resultado = 0
        return resultado
    else:
        print('Erro')
        return -1

numero = int(input('Escolha um número positivo inteiro'))

print(somaFatorial(numero))
    
