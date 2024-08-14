#FAÇA UM PROGRAMA QUE  LEIA A LARGURA E A ALTURA DE UMA PAREDE EM METROS, CALCULE A SUA ÁREA E A QUANTIDADE DE TINTA NECESSÁRIA PARA PINTA-LA N SABENDO QUE CADA LITRO DE TINTA PINTA UMA ÁREA DE 2m².

alt = float(input('Qual a Altura da parede?'))
larg = float(input('Qual a Largura da parede?'))
area = alt * larg
tinta = area/2

print('Sua parede tem a dimensão de {} x {}, e área de {:1.2f}m², será necessário {:1.2f}L de tinta para pintar a parede inteira.'.format(alt, larg, area, tinta))