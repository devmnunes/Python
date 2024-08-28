# CRIE UM PROGRAMA QUE LEIA DUAS NOTAS DE UM ALUNO E CALCULE A MÉDIA, MOSTRANDO UMA MENSAGEM NO FINAL. DE ACORDO COM A MÉDIA ATINGIDA
# MÉDIA ABAIXO DE 5.0: REPROVADO
# MÉDIA ENTRE 5.0 E 6.9: RECUPERAÇÃO
# MÉDIA ENTRE 7.0 OU SUPERIOR: APROVADO.

n1 = float(input('Digite a primeira nota: '))

n2 = float(input('Digite a segunda nota: '))

media = (n1 + n2) / 2

if media < 5.0:
    print('Sua média é {:.1f} , REPROVADO!'.format(media))
elif media == 5.0 or media <= 6.9 :
    print('Sua média é {:.1f} , RECUPERAÇÃO!'.format(media))
else:
    print('Sua média é {:.1f} , APROVADO!'.format(media))