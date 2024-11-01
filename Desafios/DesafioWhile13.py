print('-'*25)
print('   CADASTRE UMA PESSOA')
print('-'*25)
while True:
    maior = homem = mulher = 0
    idade = int(input('Idade: '))
    sexo = str(input('Sexo: [M/F] ')).upper().strip()
    if sexo == 'M':
        homem += 1
    if idade > 18:
        maior += 1
    if sexo in 'F' and idade < 20:
        mulher += 1
    print('-'*25)
    resp = str(input('Quer continuar? [S/N] ')).upper().strip()
    if resp == 'N':
        break
    if sexo == 'M':
        homem += 1
    if idade > 18:
        maior += 1
    if sexo in 'F' and idade < 20:
        mulher += 1
print(f'Total de pessoas com mais de 18 anos: {maior}.')
print(f'Ao todo temos {homem} homens cadastrados.')
print(f'E temos {mulher} mulheres com menos de 20 anos.')
print('-'*25)
