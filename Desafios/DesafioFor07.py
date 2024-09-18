#FAÇA UM PROGRAMA QUE LEIA UM NÚMERO INTEIRO E DIGA SE ELE É OU NÃO UM NÚMERO PRIMO

n = int(input('Digite um valor: '))
if n % 1 == 0 and n % n == 0:
        print('O valor {} É PRIMO! '.format(n))
else:
    print('O valor {} É PRIMO. '.format(n))
