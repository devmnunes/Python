nome = input('Digite seu nome completo: ')
nome_div = nome.split()

print('Muito prazer em te conhecer!')
print('Seu primeiro nome é {}'.format(nome_div[0])) 
print('Seu último nome é {}'.format(nome_div[-1]))