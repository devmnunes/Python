#FAÇA UM PROGRAMA QUE LEIA UM ÂNGULO QUALQUER E MOSTRE NA TELA O VALOR DO SENO, COSSENO E TANGENTE DESSE ANGULO.

import math

angulo = int(input('Digite o ângulo que você deseja: '))
se = math.sin(math.radians(angulo))
co = math.cos(math.radians(angulo))
tang = math.tan(math.radians(angulo))

print('O ângulo de {} tem o SENO de {:.2f}'. format(angulo, se))
print('O ângulo de {} tem o COSSENO de {:.2f}'. format(angulo, co))
print('O ângulo de {} tem o TANGENTE de {:.2f}'. format(angulo, tang))