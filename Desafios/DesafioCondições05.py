ano = int(input('Digite um ano: '))

if ano % 4 == 0:
 print('O ano {} é Bissexto'.format(ano))
else:
 print('O ano {} não é Bissexto'.format(ano))