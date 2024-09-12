def fib(usuario):
        anterior = 0
        proximo = 1
        indice = 1
        if usuario > 2:
                while indice  < usuario :
                        resultado = anterior + proximo
                        anterior = proximo
                        proximo = resultado
                        indice = indice + 1
                return resultado
        elif usuario == 1 or usuario == 2:
                resultado = 1
                return resultado
                        
                        
        else:
                return -1
usuario =int(input('Escolha o índice da sequência de Fibonacci a ser mostrada: '))
print(fib(usuario))
        
    
