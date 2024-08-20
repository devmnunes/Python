import random

n = [1, 2, 3, 4, 5]
sorteado = random.choices(n)
mnum = int(input('Em qual número eu estou pensando? '))
if sorteado == mnum:
    print('O número escolhido foi {}, PARABÉNS VOCÊ ACERTOU'.format(sorteado))
else:
    print('O número escolhido foi {}, TENTE NOVAMENTE!'.format(sorteado))