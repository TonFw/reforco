# TODO
letra = input('informe uma letra: ').upper()
vogais = ['A' , 'E', 'I', 'O', 'U']

if letra in vogais:
    resultado = 'vogal'
else:
    resultado = 'consoante'

print(resultado)