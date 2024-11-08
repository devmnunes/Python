lanche = ('Hamburguer', 'biscoito', 'Pizza', 'Pudim')

for pos, comida in enumerate(lanche): #Caso precise mostrar posição
    print(f'Eu vou comer {comida} na {pos}')

for cont in range (0, len(lanche)): #Caso precise mostrar posição
    print(f'Eu vou comer {lanche[cont]} na posição {cont}')
 
for comida in lanche: #Caso  não precise mostrar posição
    print(f'Eu vou comer {comida}')
          
print(sorted(lanche)) #Para colocar em ordem Alfabética

a = (2, 5, 3)
b = (6, 1, 4)
c = a + b
print(c) 
#Para mostrar quantas vezes aparece um certo valor digite c.count("valor desejado , virgula caso tenha numero repidito dai você coloca a posição ")
print(c.count(2))

#Para mostrar a posição do certo valor digite c.index("valor desejado")
print(c.index(3, 8))

pessoa = ('Matheus', 27, 'M', 65.00)
print(pessoa)
del(pessoa) #para excluir tupla