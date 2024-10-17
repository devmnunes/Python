soma = 0
contador = 0
for cont in range(1, 7):
    n = int(input('Digite um valor: '))
    if n % 2 == 0:
        contador += 1
        soma += n
print('Você informou {} números PARES e a soma foi {}'.format(contador, soma))

    