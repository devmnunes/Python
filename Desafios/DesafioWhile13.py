#CRIE UM PROGRAMA QUE LEIA A IDADE E O SEXO DE VÁRIAS PESSOAS. A CADA PESSOA CADASTRADA, O PROGRAMA DEVERÁ PERGUNTAR SE O ÚSUARIO QUER OU NÃO CONTINUAR. NO FINAL, MOSTRE:
#1 QUANTAS PESSOAS TEM MAIS DE 18 ANOS.
#2 QUANTOS HOMENS FORAM CADASTRADOS
#3 QUANTAS MULHERES TEM MENOS DE 20 ANOS.

print('-'*25)
print('   CADASTRE UMA PESSOA')
print('-'*25)
maior = homem = mulher = 0
while True:
    idade = int(input('Idade: '))
    sexo = str(input('Sexo: [M/F] ')).upper().strip()
    if sexo == 'M':
        homem += 1
    if idade > 18:
        maior += 1
    if sexo == 'F': 
        if idade < 20:
            mulher += 1
    print('-'*25)
    resp = str(input('Quer continuar? [S/N] ')).upper().strip()
    if resp == 'N':
        break
print(f'Total de pessoas com mais de 18 anos: {maior}.')
print(f'Ao todo temos {homem} homens cadastrados.')
print(f'E temos {mulher} mulheres com menos de 20 anos.')
print('-'*25)
