
n1 = int(input('Digite o 1º valor: '))
n2 = int(input('Digite o 2º valor: '))

escolha = 0 

maior = 0

soma = n1 + n2

multiplicação = n1*n2

if n1 > n2:
    maior = n1
else:
    maior = n2
    
print('---'*10)
print('[1] SOMAR')
print('[2] MULTIPLCAR')
print('[3] MAIOR')
print('[4] ESCOLHER OUTRO VALOR')
print('[5] SAIR')
print('---'*10)

while escolha == 0:
    escolha = int(input('SELECIONE UMA OPÇÃO: '))

    if escolha == 1:
        print('A soma dos valores {} e {} é igual a {}.'.format(n1, n2, soma))

    elif escolha == 2:
        print('O resultado da multiplicação dos valores {} e {} é igual a {}.'.format(n1, n2, multiplicação))

    elif escolha == 3:
         print('Entre os valores {} e {} o MAIOR valor é {}.'.format(n1, n2, maior))

    elif escolha == 4:
        n1 = int(input('Digite o 1º valor: '))
        n2 = int(input('Digite o 2º valor: '))
    
    elif escolha == 5:
        print('SAINDO DO PROGRAMA...')
        break