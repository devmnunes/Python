num = int(input('Digite um número: '))
resp = str(input('Quer continuar: [S/N]')).strip().upper()
maior = num
menor = num
while resp == 'S':
    num = int(input('Digite um número: '))
    if num < menor:
        menor = num
    if num > maior:
        maior = num
    resp = str(input('Quer continuar: ')).strip().upper()
    if resp == 'N':
        print('O maior valor foi {} e o menor foi {}.'.format(maior, menor))