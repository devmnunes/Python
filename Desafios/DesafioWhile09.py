num = int(input('Digite um número: '))
resp = str(input('Quer continuar: [S/N]')).strip().upper()
maior = num
menor = num
while resp != 'N':
    num = int(input('Digite um número: '))
    if num < menor:
        menor = num
    if num > maior:
        maior = num
    resp = str(input('Quer continuar: ')).strip().upper()
print('O maior valor foi {} e o menor foi {}.'.format(maior, menor))