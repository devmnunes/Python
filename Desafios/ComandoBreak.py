cont = 1
while cont <= 10:
    print(cont, ' ', end='')
    cont += 1
print('Acabou')

#-----------------------------------------------------------------------------------------------------

num = soma = 0
while True:
    num = int(input('Digite um número: '))
    if num == 999:
        break
    soma += num
print(f'A soma vale {soma}.')

#-----------------------------------------------------------------------------------------------------

nome ='José'
idade = 23
sal = 2631.26
print(f'O {nome} tem {idade} anos e seu salário é R${sal:.2f}.')