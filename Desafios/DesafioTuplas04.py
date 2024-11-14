#DESENVOLVA UM PROGRAMA QUE LEIA QUATRO VALORES PELO TRECLADO E GUARDE-OS EM UMA TUPLA. NO FINAL MOSTRE:
# 1- QUANTAS VEZES APARECEU O VALOR 9
# 2- EM QUE POSIÇÃO FOI DIGITADO O PRIMEIRO VALOR 3
# 3- QUAIS FORAM OS NÚMEROS PARES
val9 = 0
num = (int(input('Digite um valor: ')),
       int(input('Digite outro valor: ')),
       int(input('Digite mais um valor: ')),
       int(input('Digite o último valor: ')))
print(f' Você digitou os valores {num}')
print(f'O valor 9 apareceu {num.count(9)} vezes')
if 3 in num:
    print(f'O valor 3 apareceu na {num.index(3)+1}º posição')
else:
    print('O valor 3 não foi digitado', )
print('Os vlores pares digitados foram ', end='')
for n in num:
    if n % 2 == 0:
        print(n, end=' ')



