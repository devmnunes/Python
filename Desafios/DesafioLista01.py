#FAÇA UM PROGREAMA QUE LEIA 5 VALORES NÚMÉRICOS E GUARDE-OS EM UMA LISTA.
#NO FINAL MOSTRE QUAL FOI O MAIOR E O MENOR VALOR E SUAS RESPECTIVAS POSIÇÕES NA LISTA.

valores = list()

valores.append(int(input(f'Digite valor para a Posição 0: ')))
valores.append(int(input(f'Digite valor para a Posição 1: ')))
valores.append(int(input(f'Digite valor para a Posição 2: ')))
valores.append(int(input(f'Digite valor para a Posição 3: ')))
valores.append(int(input(f'Digite valor para a Posição 4: ')))

print('=-' * 40)

print(f'Você digitou os valores {valores}')
for c, v in enumerate (valores):
    print(f'O maior valor digitado foi o {v} que está nas posições {c}')
    
