km = float(input('Qual a distância em Km? '))

if km <= 200:
    val1 = km * 0.50
    print('Sua viajem terá a distância de {:.0f} Km, o valor da passagem será de R${:.2f}'.format(km, val1))
else:
    val1 = km * 0.45
    print('Sua viajem terá a distância de {:.0f} Km, o valor da passagem será de R${:.2f}'.format(km, val1))