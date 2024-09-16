#FAÇA UM PROGRAMA QUE LEIA UM NÚMERO INTEIRO E DIGA SE ELE É OU NÃO UM NÚMERO PRIMO

n = int(input('Digite um valor: '))
for cont in range(1, 6):
    if n % 2 == 0: 
        if n % 3 == 0:
            if n % 5 == 0:
                if n % 7 == 0:
                    if n % 11 == 0:
                        print('O valor {}  NÃO É PRIMO! '.format(n))
else:
    print('O valor {} É PRIMO. '.format(n))
