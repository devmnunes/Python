totIdade = 0
media = 0
maisVelho = 0
HomemVelho = 'Paralelepipedo'
mulher = 0
for cont in range(1,5):
    print('----- {}ª PESSOA -----'.format(cont))
    nome = str(input('Nome: ').strip())

    idade = int(input('Idade: '))
    
    sexo = str(input('Sexo [M/F]: ').upper())

    totIdade = totIdade + idade #CONTADOR DE IDADE
    media = totIdade / cont #MÉDIA DE IDADE

    if sexo in 'M': 
        if idade > maisVelho:
            maisVelho = idade
            HomemVelho = nome
    
    if sexo in 'F'and idade < 20:
        mulher = mulher + 1

print('A média de idade do grupo é {} anos. '.format(media))
print('O homem mais velho é o {}, que tem {} anos.'.format(HomemVelho, maisVelho))
print('No total {} Mulheres tem menos de 20 anos'.format(mulher))

