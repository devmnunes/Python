#ESCREVA UM PROGRAMA PARA APROVAR UM EMPRÉTIMO BANCÁRIO PARA A COMPRA DE UMA CASA, O PROGRAMA DEVE PERGUNTAR O VALOR DA CASA, O SALÁRIO DO COMPRADOR E EM QUANTOS ANOS ELE VAI PAGA.

#CALCULE O VALOR DA PRESTAÇÃO MENSAL, SABENDO QUE ELA NÃO PODE EXEDER 30% DO SALÁRIO OU ENTÃO O EMPRÉSTIMO SERÁ NEGADO

valor = float(input('Qual o valor do empréstimo: R$ '))

salario = float(input('Qual o valor do salário: R$ '))

ano = int(input('Em quantos anos você ira pagar: '))

parcelas = ano * 12
val_parce = valor / parcelas

print('Com o valor do empréstimo de R${:.2f} , o seu salário de R${:.2f} , e o prazo de {} meses, a parcela do empréstimo é de R${:.2f} '.format(valor, salario, parcelas, val_parce) )

if val_parce <= salario * 30 / 100:
    print('O empréstimo foi APROVADO!')
else:
    print('O empréstimo foi NEGADO!')