#CRIE UM PROGRAMA QUE LEIA QUANTO DINHEIRO A PESSOA TEM NA CARTEIRA E MOSTRE QUANTOS DÓLARES ELA PODE COMPRAR. CONSIDERE US$1,00 = R$5,4869

reais = float(input('Quantos dinheiro você tem? R$'))
dolar = reais / 5.48
euro = reais / 6.00
iene = reais / 26.78

print('Com o valor de R${:.2f}  você terá US${:.2f}'.format(reais, dolar))
print('Com o valor de R${:.2f}  você terá EUR{:.2f}'.format(reais, euro))
print('Com o valor de R${:.2f}  você terá JPY{:.2f}'.format(reais, iene))
