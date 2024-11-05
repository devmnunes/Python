print('-'*25)
print('   ADEGA DO INDIANO')
print('-'*25)
tot = totmil = menor = cont = 0
barato = ''
while True:
    produto = str(input('Nome do produto: ')).strip()
    valor = float(input('Preço: R$ '))
    cont += 1
    tot = tot + valor
    if valor > 1000:
        totmil += 1
    if cont == 1 or valor < menor:
        menor = valor
        barato = produto
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N]')).upper().strip()[0]
    if resp == 'N':
        break
print(f'O total de compra foi R${tot:10.2f}')
print(f'Temos {totmil} produtos custando mais de R$1000.00 ')
print(f'O produto  mais barato foi {barato} e custa R${menor}')

