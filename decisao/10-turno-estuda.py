# TODO
letra = input('informe (F ou M): ').upper()
if letra == 'F':
    resultado = 'F - Feminino'
elif letra == 'M':
    resultado = 'M - Masculino'
else:
    resultado = 'Sexo Inválido'

print(resultado)