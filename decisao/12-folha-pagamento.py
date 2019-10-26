# TODO
salario = float(input('salario: R$ '))

if salario <= 280:
    aumento_porcentagem = '20%'
    novo_salario = salario*1.2
    aumento_bruto = novo_salario - salario
elif salario > 280 and salario < 700:
    aumento_porcentagem = '15%'
    novo_salario = salario*1.15
    aumento_bruto = novo_salario - salario
elif salario > 1500:
    aumento_porcentagem = '5%'
    novo_salario = salario * 1.05
    aumento_bruto = novo_salario - salario

print('salario antes do ajuste: ', salario)
print('percentual de aumento: ', aumento_porcentagem)
print('valor do aumento: ', aumento_bruto)
print('novo salario: ', novo_salario)