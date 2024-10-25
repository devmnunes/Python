
n1 = int(input('Digite o 1º valor: '))
n2 = int(input('Digite o 2º valor: '))

escolha = 0 

maior = 0
   
print('---'*10)
print('''[1] SOMAR
[2] MULTIPLCAR
[3] MAIOR
[4] ESCOLHER OUTRO VALOR
[5] SAIR''')
print('---'*10)

while escolha == 0:
    escolha = int(input('SELECIONE UMA OPÇÃO: '))

    if escolha == 1:
        soma = n1 + n2
        print('A soma dos valores {} e {} é igual a {}.'.format(n1, n2, soma))

    elif escolha == 2:
        multiplicação = n1*n2
        print('O resultado da multiplicação dos valores {} e {} é igual a {}.'.format(n1, n2, multiplicação))

    elif escolha == 3:
         if n1 > n2:
            maior = n1
         else:
            maior = n2
         print('Entre os valores {} e {} o MAIOR valor é {}.'.format(n1, n2, maior))

    elif escolha == 4:
        print('Informe os números novamente:')
        n1 = int(input('Digite o 1º valor: '))
        n2 = int(input('Digite o 2º valor: '))
    
    elif escolha == 5:
        print('SAINDO DO PROGRAMA...')
        break