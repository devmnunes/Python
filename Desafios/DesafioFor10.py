maior = 0
menor = 0
for cont in range(1,6):
<<<<<<< Updated upstream
    peso = float(input('Digite seu peso da {}º pessoa: '.format(cont)))
    if cont == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print('O maior peso digitado foi {}Kg'.format(maior))
print('O menor peso digitado foi {}Kg'.format(menor))
=======
    peso = float(input('Digite seu peso: '))
    if cont == 0:
        maior = peso
        menor = peso
        if peso > maior:
            maior = peso
        if peso < menor:
            menor =peso
print('O maior peso digitado foi {}'.format(maior))
print('O menor peso digitado foi {}'.format(menor))
>>>>>>> Stashed changes
