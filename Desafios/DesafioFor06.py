#DESENVOLVA UM PROGRAMA QUE LEIA O PRIMEIRO TERMO E A RAZÃO DE UMA PA. NO FINAL, MOSTRE OS 10 PRIMEIROS TERMOS DESSA PROGRESSÃO

primeiro = int(input('Digite o Primeiro Termo: '))
razão = int(input('Digite a Razão: '))
décimo = primeiro + (10 - 1) * razão
for cont in range(primeiro, décimo, razão):
   print('{}'.format(cont), end='..')
print('ACABOU')