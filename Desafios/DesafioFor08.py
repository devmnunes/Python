#CRIE UM PROGRAMA QUE LEIA UMA FRASE QUALQUER E DIGA SE ELA É UM PALÍNDROMO, DESCONSIDERANDO OS ESPAÇOS

frase = str(input('Digite uma frase: ')).strip()
if frase == frase[::-1]:
    print('A frase é PALÍNDROMO')
else:
    print('A frase NÃO É PALÍNDROMO')