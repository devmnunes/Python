#Desenvolva um Programa que leia as duas notas de um aluno, calcule e mostre sua média.

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))

print('Suas notas foram {} e {}, sua média é {}'.format(n1, n2, (n1+n2)/2))