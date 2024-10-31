from random import randint
soma = 0
print('=-'*40)
print('VAMOS JOGAR PAR OU IMPAR')

while True:
    num = int(input('Diga um valor: '))
    jogador = str(input('Par ou Ímpar? [P/I] ')).upper().strip()
    computador = randint(0, 10)
    soma = computador + jogador
    if jogador == 'P' and computador == 'I'