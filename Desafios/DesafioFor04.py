#REFAÇA O DESAFIO 009, MOSTRANDO A TABUADA DE UM NÚMERO QUE O USUARIO ESCOLHER, SÓ QUE AGORA UTILIZANDO UM LAÇO FOR.

n = int(input('Digite um valor: '))
print('A TABUADA DO VALOR {} É...'.format(n))
for cont in range(1, 11): 
    resultado = n * cont
    print(n, 'x',  cont, '=', resultado)
print('FIM!')
