import random
from time import sleep

sorteado = random.randint(0, 5)
num = int(input('Em qual número eu estou pensando? '))
print('PROCESSANDO...')
sleep(2)
if sorteado == num:
    print('O número escolhido foi {}, PARABÉNS VOCÊ ACERTOU'.format(sorteado))
else:
    print('O número escolhido foi {}, e não o {} , TENTE NOVAMENTE!'.format(sorteado, num))