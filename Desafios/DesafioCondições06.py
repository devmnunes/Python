n1 = int(input('1º número: '))
n2 = int(input('2º número: '))
n3 = int(input('3º número: '))
menor = n1
maior = n2
#Verifica quem é o menor
if n2 < n1 and n2 < n3:
    menor = n2
if n3 > n1 and n3 < n2:
    menor = n3

#Verifica quem é o maior
if n1 > n2 and n1 > n3:
    maior = n1
if n3 > n1 and n3 > n2:
    maior = n3
    
print('Dos valores digitados {}, {} e {}, o MENOR número é {} e o MAIOR número é {}'.format(n1, n2, n3, menor, maior))