#CRIE UM PROGRAMA QUE LEIA A DATA DE NASCIMENTO DE 7 PESSOAS. NO FINAL, MOSTRE QUANTAS PESSOAS SÃO DE MAIOR IDADE E QUANTAS SÃO DE MENOR IDADE.

from datetime import date

maior = 0
menor = 0
atual = date.today().year

for cont in range(1, 8):
    ano = int(input('Digite seu ano de nascimento: '))
    if atual - ano < 18:
        menor = menor + 1
    else: atual - ano > 18
    maior = maior + 1
print('{} pessoas ainda são de MENOR IDADE'.format(menor))
print('{} pessoas já são de MAIORIDADE'.format(maior))

     



