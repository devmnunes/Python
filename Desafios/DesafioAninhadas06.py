# REFAÇA O DESAFIO 035 DOS TRIÂNGULOS, ACRESCENTANDO O RECURSO DE MOSTRAR QUE TIPO DE TRIANGULO SERÁ FORMADO:
# EQUILÁTERO: TODOS OS LADOS IGUAIS
# ISÓCELES: DOIS LADOS IGUAIS
# ESCALENO: TODOS OS LADOS DIFERENTES

a = float(input('Digite o valor da primeira reta: '))
b = float(input('Digite o valor da segunda reta: '))
c = float(input('Digite o valor da terceira reta: '))

if a < b + c and b < a + c and c < a + b:
    print('Com os valores {}, {} e {}, É POSSÍVEL formar um triângulo'.format(a, b, c))

if a == b == c:
     print('O triângulo formado foi o  EQUILATERO, pois todos os lados são iguais '.format(a, b, c))
elif a == b or a == c or c == b:
    print('O triângulo formado foi o  ISÓCELES, pois dois lados são iguais '.format(a, b, c))
elif a != b != c != a:
    print('O triângulo formado foi o ESCALENO, pois todos os lados são diferentes'.format(a, b, c))

else:
    print('NÃO É POSSÍVEL formar um triângulo')

    