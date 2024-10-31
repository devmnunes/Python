from random import randint
cont = soma = vitoria = 0

print('=-'*40)
print('VAMOS JOGAR PAR OU IMPAR')
print('=-'*40)

while True:
    cont += 1
    num = int(input('Diga um valor: '))
    jogador = str(input('Par ou Ímpar? [P/I] ')).upper().strip()
    computador = randint(0, 10)
    soma = num + computador

    print('-'*60)
    if soma % 2 == 0:
        print(f'você jogou {num} e o computador {computador}. Total de {soma} DEU PAR')
    else:
        print(f'você jogou {num} e o computador {computador}. Total de {soma} DEU ÍMPAR')
    print('-'*60)

    if jogador == 'P' and soma % 2 == 0:
        print('VOCÊ GANHOU')
        vitoria += 1
    elif jogador =='I'and soma % 2 == 1:
        print('VOCÊ GANHOU')
        vitoria += 1
    else:
        print('VOCÊ PERDEU')
        break
    print('=-'*40)

print(f'Você ganhou {vitoria} vezes.')


     