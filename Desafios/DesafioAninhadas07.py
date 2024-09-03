peso = float(input('Digite seu peso: '))
altura = float(input('Digite sua altura: '))
imc = peso / (altura**2)

if imc < 18.5:
    print('Seu IMC é {:.2f} , você está ABAIXO do peso. '.format(imc))
elif imc >= 18.5 and imc <= 25:
    print('Seu IMC é {:.2f} , você está no seu peso ideal, PARABENS!. '.format(imc))
elif imc >= 25 and imc <= 30:
    print('Seu IMC é {:.2f} , você está no seu SOBREPESO.'.format(imc))
elif imc >= 30 and imc <= 40:
    print('Seu IMC é {:.2f} , você está em OBESIDADE.'.format(imc))
else:
    print('Seu IMC é {:.2f} , você está em OBESIDADE MÓRBIDA.'.format(imc))