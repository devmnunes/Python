n = input('Digite algo:')

print(n)
print('O tipo primitivo desse valor é ', type(n))

print('Só tem espaços? {}'.format(n.isspace()))
print('É um número? {}' .format(n.isnumeric()))
print('É alfabético? {}' .format(n.isnumeric()))
print('É alfanúmérico? {}'.format(n.isalnum()))
print('Está em maiúsculas? {}'.format(n.isupper()))
print('Está em minúculas? {}'.format(n.islower()))
print('Está capítalizada? {}'.format(n.istitle()))