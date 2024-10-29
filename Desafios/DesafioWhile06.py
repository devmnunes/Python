#REFAÇA O DESAFIO ANTERIOR, CRIE UM PROGRAMA QUE LEIA O PRIMEIRO TERMO E A RAZÃO DE UMA PA. NO FINAL, MOSTRE OS 10 PRIMEIROS TERMOS DESSA PROGRESSÃO, E DEPOIS PERGUNTE SE QUER CONTINUAR
cont = 1
primeiro = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a Razão: '))
termo = primeiro
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while cont <= total:
        print('{} -> '.format(termo), end='')
        termo = termo + razao
        cont += 1
    print('PAUSA')
    mais = int(input('Quantos termos você quer mostrar mais? '))
print('FIM')
   