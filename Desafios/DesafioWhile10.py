#CRIE UM PROGRAMA QUE LEIA VÁRIOS NÚMEROS INTEIROS PELO TECLADO. O PROGRAMA SÓ VAI PARAR QUANDO O USUÁRIO DIGITAR O VALOR 999, QUE É A CONDIÇÃO DE PARADA. NO FINAL MOSTRE QUANTOS NÚMEROS FORAM DIGITADOS E QUAL FOI A SOMA ENTRE ELES(DESCONSIDERANDO FLAG)

num = soma = cont = 0
while True:
    num = int(input('Digite um número (999 para parar): '))
    if num == 999:
        break
    cont += 1
    soma += num
print(f'Foram digitados {cont} e a soma entre eles é {soma}.')