def quadrado(base):
    quad = base * base
    return quad

numero = int(input('número: '))

print(quadrado (numero))
resultado = quadrado(numero)

print(resultado * 5)
    
    

numero1 = float(input('Escolha um número: '))
numero2 = float(input('Escolha outro número: '))
operacao = input('Escolha a operação entre as seguintes: +,-,*,/: ')

if operacao == '+':
    print(numero1 + numero2)

elif operacao == '-':
    print(numero1 - numero2)

elif operacao == '*':
    print(numero1 * numero2)

elif operacao == '/':
    print(numero1 / numero2)

else:
    print('operação inválida')
