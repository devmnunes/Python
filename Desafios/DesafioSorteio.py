#UM PROFESSOR QUER SORTEAR UM DOS SEUS QUATRO ALUNOS PARA APAGAR O QUADRO. FAÇA UM PROGRAMA QUE AJUDE ELE, LENDO O NOME DELES E ESCREVENDO O NOME ESCOLHIDO.

import random
a1= str(input('Aluno 1: '))
a2 = str(input('Aluno 2: '))
a3 = str(input('Aluno 3: '))
a4 = str(input('Aluno 4: '))
lista = [a1, a2, a3, a4]
sorteado = random.choice(lista) #random.choice seleciona um nome aleatóriamente, já o ramdom.choices pode selecionar mais de um porém pode selecionar o mesmo nome.
print('O aluno escolhido foi {}.'.format(sorteado))

