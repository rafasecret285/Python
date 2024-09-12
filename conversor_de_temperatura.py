def celsiusParaFahrenheit(celsius):
    temperatura = celsius * 1.8 + 32
    return temperatura
def celsiusParaKelvin(celsius):
    temperatura = celsius + 273
    return temperatura


print('Conversor de celsius para Kelvin ou Fahrenheit')
celsius = float(input('Informe a temperatura em celsius: '))
converterPara = input('Selecione K para converter para celsius ou F para converter para Fahreinheit: ')

if converterPara == 'F':
    temperatura = celsiusParaFahrenheit(celsius)
    print('A temperatura em Fahreinheit é igual a',temperatura)
elif converterPara == 'K':
    temperatura = celsiusParaKelvin(celsius)
    print('A temperatura em Kelvin é igual a', temperatura)
else:
    print('Digite F ou K')
    
