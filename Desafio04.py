#ESCREVA UM PROGRAMA QUE LEIA UM VALOR EM METROS E O EXIBA EM CENTIMETRO E MILÍMETROS.

M = float(input('Digite o valor em metros:'))
c = (M * 100)
m = (M * 1000)

print('O valor {}metros é igual a {:1.0f}cm e {:1.0f}mm'.format(M, c, m))