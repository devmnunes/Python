#FAÇA UM PROGRAMA QUE LEIA O COMPRIMENTO DO CATETE OPOSTO E DO CATETE ADJACENTE DE UM TRIÂNGULO RETÂNGULO. CALCULE E MOSTRE O COMPRIMENTO DA HIPOTENUSA.

import math

co = float(input('Digite o valor do Cateto Oposto: '))
ca = float(input('Digite o valor do Cateto Adjacente: '))
h = math.acosh(co**2 + ca**2)

print('O valor da Hipotenusa é {}'.format(h))
