num = int(input('Digite um número: '))
resp = str(input('Quer continuar: [S/N]')).strip().upper()
maior = num
menor = num
total = cont = media = 0
while resp == 'S':
    num = int(input('Digite um número: '))
    cont += 1
    total += num
    if num < menor:
        menor = num
    if num > maior:
        maior = num
    resp = str(input('Quer continuar: [S/N] ')).strip().upper()
    if resp != 'NnMm':
        print('Digite uma resposta valida!!!')
        resp = str(input('Quer continuar: [S/N] ')).strip().upper()
    if resp == 'N':
        cont += 1
        total += num
media = total / cont
print('Você digitou {} números e a média foi {}.'.format(cont, media))
print('O maior valor foi {} e o menor foi {}.'.format(maior, menor))