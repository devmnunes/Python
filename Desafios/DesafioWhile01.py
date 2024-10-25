# FAÇA UM PROGRAMA QUE LEIA O SEXO DE UMA PESSOA, MAS SÓ ACEITE VALORES "M" OU "F". CASO ESTAJA ERRADO , PEÇA A DIGITAÇÃO NOVAMENTE ATÉ TER UM VALOR CORRETO.
sexo = str(input('Digite seu sexo [M/F]: ')).strip().upper()[0]
while sexo not in 'MmFf':
    sexo = str(input('Dados invalidos. Por favor, informe seu sexo: ')).strip().upper()[0]
print('Sexo {} registrado com sucesso'.format(sexo))