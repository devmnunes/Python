sal = float(input('Digite seu salário: R$'))

if sal > 1.250:
    nsal = sal + (sal * 10/100)
    print('Com base no seu antigo salário R${:.2f} , seu novo salário é R${:.2f}'.format(sal, nsal))
else:
    nsal = sal + (sal * 15/100)
    print('Com base no seu antigo salário R${:.2f} , seu novo salário é R${:.2f}'.format(sal, nsal))