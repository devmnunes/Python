#DESENVOLVA UM PROGRAMA QUE LEIA QUATRO VALORES PELO TRECLADO E GUARDE-OS EM UMA TUPLA. NO FINAL MOSTRE:
# 1- QUANTAS VEZES APARECEU O VALOR 9
# 2- EM QUE POSIÇÃO FOI DIGITADO O PRIMEIRO VALOR 3
# 3- QUAIS FORAM OS NÚMEROS PARES
cont = val9 = 0
valores = []
while True:
    cont+= 1
    num = int(input(f'Digite o {cont}º valor: '))
    if num == 9:
        val9 += 1
    valores.append(num)
    if cont == 4:
        break
valores = tuple(valores)
print(valores)