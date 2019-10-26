lado1 = float(input('informe a lado1: '))
lado2 = float(input('informe a lado2: '))
lado3 = float(input('informe a lado3: '))

if lado1 + lado2 > lado3 and lado2 + lado3 > lado1 and lado1 + lado3 > lado2:
    eh_triangulo = True
else:
    eh_triangulo = False

if not eh_triangulo:
    print('Os lados informados não formam um triangulo')
    exit(0)

if lado1 == lado2 or lado1 == lado3:
    if lado2 == lado3:
        triangulo = 'equilátero'
    else:
        triangulo = 'isósceles'
elif lado1 != lado2 and lado1 != lado3 and lado2 != lado3:
    triangulo = 'escaleno'

print('o triangulo informado é: ', triangulo)