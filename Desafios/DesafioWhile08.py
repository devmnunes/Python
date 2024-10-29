#DIGITE O VALOR 777 PARA PARAR:
soma = 0
cont = 0
num = 0
while num != 777:
    num = int(input('Digite um número ou [777 para parar]: '))
    if num != 777:
        soma = soma + num 
        cont += 1
print('Você digitou {} números e a soma entre eles foi {}.'.format(cont, soma))