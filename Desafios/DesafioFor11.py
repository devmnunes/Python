totIdade = 0
media = 0
maisVelho = 0
HomemVelho = 'João'
mulher = 0
for cont in range(1,5):
    nome = str(input('Nome da {}º pessoa: '.format(cont))).strip()

    idade = int(input('Idade da {}º pessoa: '.format(cont)))
    totIdade = totIdade + idade

    sexo = str(input('Sexo da {}º pessoa: '.format(cont))).strip()

    media = totIdade / cont

    if sexo == 'homem': 
        if idade > maisVelho:
            maisVelho = idade
            HomemVelho = nome
    

    if sexo == 'mulher'and idade < 20:
        mulher = mulher + 1

print('A média de idade do grupo é {} anos. '.format(media))
print('O homem mais velho é o {}, que tem {} anos.'.format(HomemVelho, maisVelho))
print('No total {} Mulheres tem menos de 20 anos'.format(mulher))

