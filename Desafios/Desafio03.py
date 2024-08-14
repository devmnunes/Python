#Desenvolva um Programa que leia as duas notas de um aluno, calcule e mostre sua média.

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
media = (n1 + n2) / 2

print('Suas notas foram {:.1f} e {:.1f}, sua média é {:.1f}'.format(n1, n2, media))