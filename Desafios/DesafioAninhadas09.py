import random
from time import sleep

itens = ('Pedra', 'Papel', 'Tesoura' )

computador = random.randint(1, 3)

jogador =  int(input('''Vamos jogar Jokenpô:
                    
    [1] PEDRA
    [2] PAPEL
    [3] TESOURA
        
    Qual sua escolha ? '''))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO')



print('-=' * 13)

print('Computador jogou {}'. format(itens[computador]))

print('Jogador jogou {}'.format(itens[jogador]))

print('-=' * 13)

if computador == 1: #Computador jogou Pedra
    if jogador == 1:
        print('EMPATE')
    elif jogador == 2:
        print('JOGADOR VENCE')
    elif jogador == 3:
         print('COMPUTADOR VENCE')
    else:
        print('JOGADA INVALIDA')

elif computador == 2: #Computador jogou Papel

    if jogador == 1:
        print('COMPUTADOR VENCE')   
    elif jogador == 2:
        print('EMPATE')
    elif jogador == 3:
        print('JOGADOR VENCE')
    else:
        print('JOGADA INVALIDA')
    
elif computador == 3: #Computador jogou Tesoura

    if jogador == 1:
        print('JOGADOR VENCE')   
    elif jogador == 2:
        print('COMPUTADOR VENCE')
    elif jogador == 3:
        print('EMPATE')
else:
        print('JOGADA INVALIDA')
    

