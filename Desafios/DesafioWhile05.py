#REFAÇA O DESAFIO 051, PROGRAMA QUE LEIA O PRIMEIRO TERMO E A RAZÃO DE UMA PA. NO FINAL, MOSTRE OS 10 PRIMEIROS TERMOS DESSA PROGRESSÃO

cont = 1
primeiro = int(input('Digite o Primeiro Termo: '))
razão = int(input('Digite a Razão: '))
termo = primeiro
while cont <= 10:
   print('{} -> '.format(termo), end='')
   termo = termo + razão
   cont += 1
print('ACABOU')

