#FAÇA UM PROGRAMA QUE LEIA UM NÚMERO QUALQUER E MOSTRE O SEU FATORIAL.
#EX: 5! = 5*4*3*2*1=120

cont = 1
fatorial = 1
num = int(input('Digite um valor: '))

while cont <= num:
     fatorial *= cont
     cont += 1

print('O resultado da fatoração do valor {} é {}.'.format(num, fatorial))

