#FAÇA UM PROGRAMA QUE CALCULE A SOMA ENTRE TODOS OS NÚMEROS (ÍMPARES) QUE SÃO MULTIPLOS DE TRÊS E QUE SE ENCONTRAM NO INTERVALO DE 1 A 500.

s = 0
mult = 0

for cont in range(1, 500+1):
    if (cont / 2) % 1 and cont * 3:
        mult = mult + cont
print(mult)
