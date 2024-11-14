#CRIE UM PROGRAMA QUE VAI GERAR CINCO NÚMEROS ALEATÓRIOS E COLOCAR EM UMA TUPLA.

#DEPOIS DISSO, MOSTREA LISTAGEM DE NÚMEROS GERADOS E TAMBÉM INDIQUE O MENOR E O MAIOR VALOR QUE ESTÃO NA TUPLA.

from random import randint
tupla = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))
maior = max(tupla)
menor = min(tupla)
print(tupla)
print(f' O maior valor sorteado foi {maior}')
print(f' O menor valor sorteado foi {menor}')