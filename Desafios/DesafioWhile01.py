# FAÇA UM PROGRAMA QUE LEIA O SEXO DE UMA PESSOA, MAS SÓ ACEITE VALORES "M" OU "F". CASO ESTAJA ERRADO , PEÇA A DIGITAÇÃO NOVAMENTE ATÉ TER UM VALOR CORRETO.
sexo = ''
masculino = 'MASCULINO'
feminino = 'FEMININO'
while sexo != 'M' and sexo != 'F':
    print('VALOR NÃO VALIDO, DIGITE NOVAMENTE!!!')
    sexo = str(input('Digite seu sexo [M/F]: ')).upper()
if sexo == 'F':
    sexo = feminino 
if sexo == 'M':
    sexo = masculino
print('SEXO INSERIDO {}'.format(sexo))