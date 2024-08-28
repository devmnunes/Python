#ESCREVA UM PROGRAMA QUE LEIA UM NÚMERO INTEIRO QUALQUER E PEÇA PARA O ÚSUARIO ESCOLHER QUAL SERÁ A BASE DE CONVERSÃO: 
#1 DECIMAL
#2 OCTAL
#3 HEXADECIMAL

num = int(input('Digite um valor: '))



base = int(input('''qual a base de conversão:   
                    
        1 Decimal
        2 Octal
        3 Hexadecimal
        
        Qual sua escolha ? '''))
    
if base == 1:
    print('O valor {} em Binário fica {}. '.format(num, bin(num))) 

elif base == 2:
    print('O valor {} em Octal fica {}. '.format(num, oct(num))) 

elif base == 3:
    print('O valor {} em Hexadecimal fica {}. '.format(num, hex(num))) 

