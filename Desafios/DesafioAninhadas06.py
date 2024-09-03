a = float(input('Digite o valor da primeira reta: '))
b = float(input('Digite o valor da segunda reta: '))
c = float(input('Digite o valor da terceira reta: '))

if a < b + c and b < a + c and c < a + b:
    print('Com a junção das retas {}, {} e {} é possível formar um triângulo. '.format(a, b, c))
if a == b == c:
    print('Como todos os lados são iguais, o triângulo formado foi do tipo: EQUILÁTERO. ')
elif a == b or a == c or c == b:
    print('Como apenas dois lados são iguais, o triângulo formado foi do tipo: ISÓSCELES.')
elif a != b != c:
    print('Como nenhum dos lados são iguais, o triângulo formado foi do tipo: ESCALENO.')
else:
    print('Não é possível formar um triangulo com as retas {}, {} e {}. '.format(a, b, c))

