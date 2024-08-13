# + = ADIÇÃO                            #1 ()
# - = SUBTRAÇÃO                         #2 **
# * = MULTIPLICAÇÃO                     #3 *, /, //, %
# / = DIVISÃO                           #4 +, -
# ** = POTÊNCIA
# // = DIVISÃO INTEIRA
# % = RESTO DA DIVISÃO

n1= int(input('Digite um valor: '))
n2 = int(input('digite outro valor: '))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2
res = n1 % n2

print('A Soma é {}, \n o produto é {} \n e a divisão é {:1.3f}'.format(s, m, d))
print('A Divisão interia {} a potência {} e o resto da divisão é {}'. format(di, e, res))
