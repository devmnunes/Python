r1 = float(input(' Primerira Reta: '))
r2 = float(input(' Segunda Reta: '))
r3 = float(input(' Terceira Reta: '))

if r1 + r2 > r3 :
    print('Os valores das retas {} , {} e {} , formam um triângulo. '.format(r1, r2, r3))
elif r1 + r3 > r2:
    print('Os valores das retas {} , {} e {} , formam um triângulo. '.format(r1, r2, r3))
elif r2 + r3 > r1:
    print('Os valores das retas {} , {} e {} , formam um triângulo. '.format(r1, r2, r3))
else:
    print('Os valores {} , {} e {} , não formam um triângulo.'.format(r1, r2, r3))