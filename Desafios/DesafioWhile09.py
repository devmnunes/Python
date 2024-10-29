num = int(input('Digite um valor: '))
resp = str(input('Deseja continuar [S/N]: ')).upper().strip()
cont = total = media = maior = menor = 0
maior = num
menor = num
while resp not in 'N':
    num = int(input('Digite um valor: '))
    cont += 1
    total = total + num
    resp = str(input('Deseja continuar [S/N]: ')).upper().strip()
if resp == 'N':
    cont += 1
    total = total + num
if cont == 1:
        maior = menor = num
else:
    if num > maior:
         maior = num
    if num < menor:
        menor = num
media = total / cont
print('Você digitou {} números e a média deles é {}.'.format(cont, media))
print('O maior número digitado foi {} e o menor foi {}.'.format(maior, menor))