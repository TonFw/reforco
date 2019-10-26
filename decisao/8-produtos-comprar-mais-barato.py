produto1 = input('Informe o nome do produto 1: ')
valor1 = float(input('informe o valor do produto: R$ '))

produto2 = input('Informe o nome do produto 2: ')
valor2 = float(input('informe o valor do produto: R$ '))

produto3 = input('Informe o nome do produto 3: ')
valor3 = float(input('informe o valor do produto: R$ '))

if valor1 < valor2 and valor1 < valor3:
    resultado = produto1
elif valor2 < valor1 and valor2 < valor3:
    resultado = produto2
elif valor3 < valor1 and valor3 < valor2:
    resultado = produto3

print('deve comprar o:', resultado)