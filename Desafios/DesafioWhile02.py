import random
computador = random.randint(0, 10)
acertou = False
cont = 0
while not acertou:
        cont += 1
        jogador = int(input('Em qual numero eu estou pensando? '))
        print('Você errou, tente novamente!')
        if jogador == computador:
          acertou = True
print('PARABÉNS VOCÊ ACERTOU, O NÚMERO ESCOLHIDO FOI {}, VOCÊ PRECISOU DE {} TENTATIVAS PARA ACERTAR.'.format(jogador, cont))
        

        

    