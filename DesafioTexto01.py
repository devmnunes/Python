# CRIE UM PROGRAMA QUE LEIA O NOME COMPLETO DE UMA PESSOA E MOSTRE:
# O NOME COM TODAS AS LETRAS MAIÚSCULAS E MINÚSCULAS.
# QUANTAS LETRAS TEM O NOME COMPLETO (SEM CONSIDERAR ESPAÇOS).
# QUANTAS LETRAS TEM O PRIMEIRO NOME.


nome = input('Digite seu nome completo: ')
novo_nome = nome.replace(" ", "")
primeiro = nome.split()

print('Analisando seu nome...')

print('Seu nome em maiúsculas é {} '.format(nome.upper()))
print('Seu nome em minúsculas é {} '.format(nome.lower()))
print('Seu nome tem ao todo {} letras '.format(len(novo_nome)))
print('Seu primeiro nome é {} e ele tem {} letras '.format(primeiro[0], len(primeiro[0])))
      
      
      