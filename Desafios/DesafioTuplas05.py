print('-' * 40)
print(f'{"LISTAGEM DE PREÇOS":^40}')
print('-' * 40)

lista = ('Lápis', 1.75,
         'Borracha', 2.00,
         'Caderno', 15.00,
         'Estojo', 25.00,
         'Transferidor', 4.20,
         'Compasso', 10.00,
         'Mochila', 120.00,
         'Canetas', 22.50,
         'Livro', 34.90)
for pos in range(0, len(lista)):
    if pos % 2 == 0:
        print(f'{lista[pos]:.<30}', end=' ')
    else:
        print(f'R${lista[pos]:>7.2f}')
print('-' * 40)