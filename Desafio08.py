#FAÇA UM ALGORITIMO QUE LEIA O PREÇO DE UM PRODUTO E MOSTRE SEU NOVO PREÇO COM 5% DE DESCONTO.

valor = float(input('Digite o valor do produto: '))
desc = valor * 5/100
nvalor = valor - desc

print('O produto com o valor R${:1.0f} Reais, com o desconto de ficará R${:1.0f} Reais.'.format(valor, nvalor))