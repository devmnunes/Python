import math 

#OU PODEMOS IMPORTA ALGO ESPECIFICO DO DICÍONARIO MATH ESCREVENDO FROM > MATH > IMPORT > ESCOLHA A FUNCIONALIDADE DESEJADA.

num = int(input('Digite um número: '))
raiz = math.sqrt(num)
print('A raiz quadrada do valor {} é {}'.format(num, math.ceil(raiz)))