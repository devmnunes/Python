import random

jogador =  int(input('''Vamos jogar Jokenpô:
                    
       1 - Pedra
       2 - Papel
       3 - Tesoura
        
    Qual sua escolha ? '''))

maquina = random.randint(1, 3)

if jogador == 1 and maquina == 2:
    print('Você escolheu PEDRA, e eu escolhi PAPEL, você PERDEU! ')

elif jogador == 1 and maquina == 3:
    print('Você escolheu PEDRA, e eu escolhi TESOURA, você GANHOU! ') 

elif jogador == 1 and maquina == 1:
    print('EMPATE JOGAR NOVAMENTE!')

elif jogador == 2 and maquina == 1:
    print('Você escolheu PAPEL, e eu escolhi PEDRA, você GANHOU! ')

elif jogador == 2 and maquina == 3:
    print('Você escolheu PAPEL, e eu escolhi TESOURA, você PERDEU!')

elif jogador == 2 and maquina == 2:
    print('EMPATE JOGAR NOVAMENTE!')

elif jogador == 3 and maquina == 1:
    print('Você escolheu TESOURA, e eu escolhi PEDRA, você PERDEU! ')

elif jogador == 3 and maquina == 2:
    print('Você escolheu TESOURA, e eu escolhi PAPEL, você GANHOU! ')

elif jogador == 3 and maquina == 3:
    print('EMPATE JOGAR NOVAMENTE!')

else:
    print('Esse valor não é valido')