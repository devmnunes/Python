#FAÇA UM PROGRAMA QUE LEIA O ANO DE NASCIMENTO DE IM JOVEM E INFORME, DE ACORDO COM SUA IDADE:
#SE ELE AINDA VAI SE ALISTAR AO SERVIÇO MILITAR
#SE É A HORA DE SE ALISTAR
#SE JÁ PASSOU DO TEMPO DO ALISTAMENTO

from datetime import date

nasc = int(input('Em que ano você nasceu? '))

ano = date.today().year

idade = ano - nasc

temp = idade - 18


if idade < 18:
    print(' Sua idade é {} VOCÊ AINDA NÃO TEM IDADE PARA SE ALISTAR, faltam {} anos'.format(idade, temp))

elif idade == 18:
    print('Sua idade é {} , ESTA NA HORA DE SE ALISTAR'.format(idade))

else:
    print('Sua idade é {} , JÁ PASSOU {} ANOS DO TEMPO DO ALISTAMENTO'.format(idade, temp))


