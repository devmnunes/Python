import random
from time import sleep

sorteado = random.randint(0, 5)
num = int(input('Em qual número eu estou pensando? '))
print('PROCESSANDO...')
sleep(2)
if sorteado == num:
    print(f'O número escolhido foi {sorteado}, PARABÉNS VOCÊ ACERTOU')
else:
    print('O número escolhido foi {}, e não o {} , TENTE NOVAMENTE!'.format(sorteado, num))