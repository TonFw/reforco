n1 = int(input('informe a nota1: '))
n2 = int(input('informe a nota2: '))
media = (n1+n2)/2

if media == 10:
    resultado = 'Aprovado com Distinção'
elif media >= 7:
    resultado = 'Aprovado'
else:
    resultado = 'Reprovado'

print(resultado)