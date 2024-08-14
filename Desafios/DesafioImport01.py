#CRIE UM PROGRAMA QUE LEIA UM NÚMERO REAL QUALQUER PELO TECLADO E MOSTRE NA TELA A SUA PORÇÃO INTEIRA

import math

num = float(input('Digite um número'))
nint = math.floor(num)

print('O número {} tem a parte inteira {}'. format(num, nint))