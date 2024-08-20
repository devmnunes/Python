limite_vel = 80
vel = float(input('Qual a velocidade do veículo'))
excesso = vel - limite_vel
valor = excesso * 7

if vel <= 80:
    print('Sua velocidade é de {}Km, você está dentro do limite de velocidade'.format(vel))
else:
    print('Sua velocidade é de {}Km, você foi MULTADO por excesso de velocidade, o valor da multa é de R${:.2f} Reais. '.format(vel, valor))