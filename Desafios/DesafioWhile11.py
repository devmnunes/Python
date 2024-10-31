#FAÇA UM PROGRAMA QUE MOSTRE A TABUADA DE VÁRIOS NÚMEROS, UM DE CADA VALOR DIGITADO. O PROGRAMA SERÁ INTERROMPIDO QUANDO O NÚMERO SOLICITADO FOR NEGATIVO.
while True:
    num = int(input('Qual tabuada você quer ver? '))
    if num < 0:
        break
    print('-' * 40)
    for cont in range(1, 11):
        print(f'{num} x {cont} = {num*cont}')
    print('-' * 40)
print('PROGRAMA ENCERRADO')