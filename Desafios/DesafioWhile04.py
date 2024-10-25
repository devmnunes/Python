#FAÇA UM PROGRAMA QUE LEIA UM NÚMERO QUALQUER E MOSTRE O SEU FATORIAL.
#EX: 5! = 5*4*3*2*1=120

num = int(input('Digite um valor: '))
cont = num
f = 1 
print('Calculando {}! = '.format(num), end='')
while cont > 0:
    print('{}'.format(cont), end='')
    print(' x ' if cont > 1 else ' = ', end='')
    f *= cont
    cont -= 1
print(f, end='')

