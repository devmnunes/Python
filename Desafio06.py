#CRIE UM PROGRAMA QUE LEIA QUANTO DINHEIRO A PESSOA TEM NA CARTEIRA E MOSTRE QUANTOS DÓLARES ELA PODE COMPRAR. CONSIDERE US$1,00 = R$5,4869

reais = float(input('Quantos Reais você tem?'))
dolar = reais / 5,48

print('Com o valor de R${} Reais você terá US${} Dólares'.format(reais, dolar))
