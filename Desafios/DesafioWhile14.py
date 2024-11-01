print('-'*25)
print('   ADEGA DO INDIANO')
print('-'*25)
tot = prodMil = 0
while True:
    produto = str(input('Nome do produto: ')).strip()
    valor = float(input('Preço: R$ '))
    resp = ''
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N]')).upper().strip()[0]
    if resp in 'N':
        break

print(f'O total de compra foi R${tot:.2f}')
print(f'Temos {prodMil} produtos custando mais de R$1000.00 ')

