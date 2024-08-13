#CRIE UM ALGORITIMO QUE LEIA UM NÚMERO E MOSTRE O SEU DOBRO, TRIPLO E RAIZ QUADRADA.

n = int(input('Digite um valor:'))

print('O dobro do valor {} é {}, o triplo é {}, e a raiz quadrada é {:1.3f}'.format(n, n*2, n*3, n**(1/2)))