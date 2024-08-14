#CRIE UM ALGORITIMO QUE LEIA UM NÚMERO E MOSTRE O SEU DOBRO, TRIPLO E RAIZ QUADRADA.

n = int(input('Digite um valor:'))
d = n*2
t = n*3
raizq = n**(1/2)

print('O dobro do valor {} é {}.\n O triplo de {} é {}. \n A raiz quadrada de {} é {:1.2f}'.format(n, d, n, t, n, raizq))