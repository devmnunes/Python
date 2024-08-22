#CRIE UM PROGRAMA QUE LEIA TRÊS RETAS, E VEJA SE É POSSÍVEL FORMAR UM TRIÂNGULO.

a = float(input('Primerira Reta: '))
b = float(input('Segunda Reta: '))
c = float(input('Terceira Reta: '))

if  a < b + c and b < a + c and c < a + b:
    print('Com os valores {}, {} e {}, É POSSÍVEL formar um triângulo'.format(a, b, c))
else:
    print('Com os valores {}, {} e {}, NÃO É POSSÍVEL formar um triângulo'.format(a, b, c))