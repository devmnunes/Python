for contador in range(1, 7): #Contador Númérico
    print(contador)
print('FIM')

XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

for contador in range(1, 7, -1): #Contador Númérico de trás para frente
    print(contador)
print('FIM')

XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

for contador in range(0, 7, 2): #Contador Númérico pulando de 2 em 2
    print(contador)
print('FIM')

XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

n = int(input('Digite um número: '))
for cont in range(0, n+1):
        print(cont)
print('FIM')

XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

i = int(input('Inicio: '))
f = int(input('Fim: '))
p = int(input('Passo: '))
for cont in range(i, f+1, p):
    print(cont)
print('FIM')

XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

s = 0
for cont in range(0, 4):
     n = int(input('Digite um valor: '))
     s += n
print('A soma de todos os números é {}'.format(s))