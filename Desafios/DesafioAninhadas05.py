# A CONFEDERAÇÃO NACIONAL DE NATAÇÃO PRECISA DE UM PROGRAMA QUE LEIA O ANO DE NASCIMENTO DE UM ATLETA E MOSTRE SUA CATEGORIA , DE ACORDO COM A IDADE:
# ATÉ 9 ANOS: MIRIM
# ATÉ 14 ANOS: INFANTIL
# ATÉ 19 ANOS: JUNIOR
# ATÉ 20 ANOS: SÊNIOR
# ACIMA: MASTER

from datetime import date

nasc = int(input('Digite seu ano de nascimento: '))

ano = date.today().year

idade = ano - nasc

if idade <= 9:
    print('Você tem {} anos, sua categoria é "MIRIM" '.format(idade))
elif idade <= 14:
    print('Você tem {} anos, sua categoria é "INFANTIL" '.format(idade))
elif idade <= 19:
    print('Você tem {} anos, sua categoria é "JUNIOR" '.format(idade))
elif idade <= 20:
    print('Você tem {} anos, sua categoria é "SÊNIOR" '.format(idade))
else:
    print('Você tem {} anos, sua categoria é "MASTER" '.format(idade))


