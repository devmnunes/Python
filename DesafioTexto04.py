nome = input('Digite seu nome completo: ')
nome_sep = nome.strip()

print('Seu nome tem Silva? {}'.format('silva' in nome_sep.lower()))