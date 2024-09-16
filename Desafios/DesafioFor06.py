#DESENVOLVA UM PROGRAMA QUE LEIA O PRIMEIRO TERMO E A RAZÃO DE UMA PA. NO FINAL, MOSTRE OS 10 PRIMEIROS TERMOS DESSA PROGRESSÃO

n = int(input('Digite o Primeiro Termo: '))
r = int(input('Digite a Razão: '))

print('A Progressão Aritimética do valor {} com a Razão {} é...'.format(n, r))
for cont in range(n, 11, r):
   print(cont)