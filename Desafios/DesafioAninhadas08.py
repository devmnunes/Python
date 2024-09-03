valor = float(input('Qual valor do produto: R$ '))

pag = int(input('''qual a forma de pagamento:   
                    
        1 = Dinheiro - 10% Desconto
        2 = Avista no Cartão - 5% Desconto
        3 =  Cartão até 2x - Preço Normal
        4 = 3x ou mais no Cartão - Juros 20%
        
        Qual sua escolha ? '''))

if pag == 1:
    pag = valor - valor*(10/100)
    print('Como a forma de pagamento é á vista no dinheiro você recebeu um desconto de 10% , o novo valor do produto é R${:.2f} .'.format(pag))
elif pag == 2:
    pag = valor - valor*(5/100)
    print('Como a forma de pagamento foi à vista no cartão você recebeu um desconto de 5% , o novo valor pago do produto é R${:.2f} .'.format(pag))
elif pag == 3:
    pag = valor
    print('Como a forma de pagamento foi parcelado em 2x no cartão você não receberá desconto , o valor do produto continua o mesmo R${:.2f} .'.format(pag))
elif pag == 4:
    pag = valor + valor*(20/100)
    print('Como a forma de pagamento foi parcelado em 3x ou mais no cartão paragá o valor com Juros de 20% , o novo valor do produto é R${:.2f} .'.format(pag))
else:
    print('Digite uma forma de pagamento valida')