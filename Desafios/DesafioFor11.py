totIdade = 0
maisVelho = 0
HomemVelho = 'João'
for cont in range(1,3):
    nome = str(input('Nome da {}º pessoa: '.format(cont)))

    idade = int(input('Idade da {}º pessoa: '.format(cont)))
    totIdade = totIdade + idade

    media = totIdade / cont

    sexo = str(input('Sexo da {}º pessoa: '.format(cont)))
    listaSexo = sexo.split()

    if sexo == 'Homem':
        if idade > maisVelho:
            HomemVelho = nome
    

print('A média de idade do grupo é {} anos. '.format(media))
print('O homem mais velho é o {}, que tem {} anos.'.format(HomemVelho, idade))
