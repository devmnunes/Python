#REFAÇA O DESAFIO 051, PROGRAMA QUE LEIA O PRIMEIRO TERMO E A RAZÃO DE UMA PA. NO FINAL, MOSTRE OS 10 PRIMEIROS TERMOS DESSA PROGRESSÃO

cont = 1
primeiro = int(input('Digite o Primeiro Termo: '))
razão = int(input('Digite a Razão: '))
décimo = primeiro + (10 - 1) * razão
while not décimo:
   
   
   print('{}'.format(cont), end='..')
print('ACABOU')

