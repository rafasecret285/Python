def exponenciacao(expoente,baseinicial):
    cont = 1
    base = baseinicial
    
    if expoente > 1:
        while cont < expoente:
            novabase = baseinicial * base
            base = novabase
            cont = cont + 1
            resultado = novabase
            

    elif expoente == 0:
        resultado = 1

    elif expoente == 1:
        resultado = base

    else:
        resultado = 'erro'

    return resultado

baseinicial = int(input('Escolha a base inteira para sua exponenciação: '))
expoente = int(input('Escolha o expoente inteiro positivo para sua operação: '))
print(exponenciacao(expoente,baseinicial))
