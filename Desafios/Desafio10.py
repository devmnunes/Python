#FAÇA UM ALGORITIMO QUE FAÇA CONVERSÕES DE TEMPERATURAS.

c = float(input('Informe a temperatura em °C:'))
f = (c * 1.8) + 32
k = (c + 273.15)

print('A temperatura de {}°C corresponde a {}°F, e {}°K !'.format(c, f, k))
