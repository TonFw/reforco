a = float(input('informe o "a" da função: '))
if a == 0:
    print('esta não é uma função de segundo grau (a deve ser maior do que 0')
    exit(0)

b = float(input('informe o "b" da função: '))
c = float(input('informe o "c" da função: '))

delta = (b**2) - (4*a*c)
if delta < 0:
    print('a equação não possui raizes reais (delta negativo)')
    exit(0)
elif delta == 0:
    print('a equação possui apenas uma raíz real')
    exit(0)
else:
    x1 = (-b + ((b**2 - 4*a*c) ** (1/2))) / 2*a
    x2 = (-b - ((b**2 - 4*a*c) ** (1/2))) / 2*a
    print('raízes (x1 e x2) da equação: ', x1,x2)