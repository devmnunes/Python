#CRIE UMA TUPLA PREENCHIDA COM OS 20 PRIMEIROS COLOCADOS DA TABELA DO CAMPEONATO BRASILEIRO DE FUTEBOL, NA ORDEM DE COLOCAÇÃO, DEPOIS MOSTRE: 
#APENAS OS 5 PRIMEIROS COLOCADOS.
#OS ÚTIMOS 4 COLOCADOS DA TABELA.
#UMA LISTA COM OS TIMES EM ORDEM ALFABÉTICA.
#EM QUE POSIÇÃO NA TABELA ESTÁ O TIME CHAPECOENSE.

times = ('São Paulo', 'Palmeiras', 'Santos', 'Vasco', 'Fluminense', 'Botafogo', 'Flamengo', 'Cruzeiro', 'Atletico Mineiro', 'Bahia', 'Vitória', 'Fortaleza', 'Internacional', 'Gremio', 'Atletico Paranaense', 'Ponte Preta', 'Chapecoense', 'Sporte', 'Curitiba', 'Corinthians')
print('-='*45)
print(f'Tabela Brasileirão 2024: {times}')
print('-='*45)
print(f'Os 5 primeiros são {times[:5]}')
print('-='*45)
print(f'Os 4 últimos são {times[16:]}')
print('-='*45)
print(f'Times em ordem alfabética: {sorted(times)}')
print('-='*45)
print(f' A Chapecoense está na {times.index('Chapecoense')}º posição')