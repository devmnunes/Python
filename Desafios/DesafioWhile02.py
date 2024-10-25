import random
from time import sleep

cont = 0
num = int(input('Em qual numero eu estou pensando? '))
print('PROCESSANDO...')
sleep(2)
sorteio = random.randint(1, 5)
while not sorteio == num:
        cont += 1
        sorteio = random.randint(1, 11)
        print('O número escolhido foi {}, e não o {} , TENTE NOVAMENTE!'.format(sorteio, num))
        num = int(input('Em qual numero eu estou pensando? '))
 
print('O numero escolhido foi {}, PARABÉNS VOCÊ ACERTOU, foram necessárias {} tentativas!!!'.format(sorteio, cont))
    