#FAÇA UM PROGRAMA QUE CALCULE A SOMA ENTRE TODOS OS NÚMEROS (ÍMPARES) QUE SÃO MULTIPLOS DE TRÊS E QUE SE ENCONTRAM NO INTERVALO DE 1 A 500.

soma = 0
contador = 0
for cont in range(1, 501, 2):
        if cont % 3 == 0: #Calcula os números ímpares multiplos de 3
            contador += 1
            soma += cont
print('A soma de todos os {} valores é {} '.format(contador, soma))