#FAÇA UM ALGORITIMO QUE LEIA O SALÁRIO DE UM FUNCIONÁRIO E FAÇA UM REAJUSTE DE 15% DE AUMENTO.

sal = float(input('Qqual é o salário do Funcionario? R$'))
nsal = sal + (sal * 15/100)

print('Um funcionário que ganhava R${:.2f}, com 15% de aumento, passa a receber R${:.2f}.'.format(sal, nsal))