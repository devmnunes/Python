#FAÇA UM PROGRAMA QUE MOSTRE A TABUADA DE VÁRIOS NÚMEROS, UM DE CADA VALOR DIGITADO. O PROGRAMA SERÁ INTERROMPIDO QUANDO O NÚMERO SOLICITADO FOR NEGATIVO.

cont = 0
while True:
    num = int(input('Quer ver a tabuada de qual valor? '))
    print(f'-'*40)
    while cont < 10:
        cont += 1
        resultado = num *cont
        print(f'{num} x {cont} = {resultado}')