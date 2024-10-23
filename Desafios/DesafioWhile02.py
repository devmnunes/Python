import random
from time import sleep

cont = 0
sorteio = random.randint(0, 10)
num = int(input('Em qual número eu estou pensando? '))
print('PROCESSANDO...')
sleep(2)
while not sorteio == num:
    cont += 1
    print('O número escolhido foi {}, e não o {} , TENTE NOVAMENTE!'.format(sorteio, num))
    num = int(input('Em qual número eu estou pensando? '))
if sorteio == num:
    print('O número escolhido foi {}, PARABÉNS VOCÊ ACERTOU, foram necessárias {} tentativas!!!'.format(sorteio, cont))
    