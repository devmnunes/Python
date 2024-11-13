#DESENVOLVA UM PROGRAMA QUE LEIA QUATRO VALORES PELO TRECLADO E GUARDE-OS EM UMA TUPLA. NO FINAL MOSTRE:
# 1- QUANTAS VEZES APARECEU O VALOR 9
# 2- EM QUE POSIÇÃO FOI DIGITADO O PRIMEIRO VALOR 3
# 3- QUAIS FORAM OS NÚMEROS PARES
val9 = 0
tupla_par = ()
n1 = int(input('Digite o 1º valor: '))
if n1 == 9:
    val9 += 1
if n1 % 2 == 0:
    tupla_par = (n1)
n2 = int(input('Digite o 2º valor: '))
if n2 == 9:
    val9 += 1
if n2 % 2 == 0:
    tupla_par = (n2)
n3 = int(input('Digite o 3º valor: '))
if n3 == 9:
    val9 += 1
if n3 % 2 == 0:
    tupla_par = (n3)
n4 = int(input('Digite o 4º valor: '))
if n4 == 9:
    val9 += 1
if n4 % 2 == 0:
    tupla_par = (n4)
tupla = (n1, n2, n3, n4)

print(tupla)
print(f'O valor 9 aparece {val9} vezes.')
print(f'O primeiro valor 3 aparece na posição {tupla.index(3)}')
print(f'Os valores pares são {tupla_par}')






