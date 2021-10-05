print('-----REGRA DE TRÊS-----')
from time import sleep
n1 = n2 = n3 = n4 = total = 0
continuar = ''
#Laço principal se encerrado, encerra o programa
while True:
    print('Digite o número 0 caso você não saiba o valor...')
    n1 = float(input('Digite o primeiro valor: '))
    n2 = float(input('Digite o segundo valor: '))
    n3 = float(input('Digite o terceiro valor: '))
    n4 = float(input('Digite o quarto valor: '))
    print(f'''         {n1} ----- {n2}
         {n3} ----- {n4}''')
    #ONDE É FEITO TODOS OS CÁLCULOS
    if n1 == 0:
        total = n2 * n3
        total /= n4
        print(f'O resultado da regra de três é {total}.')
    elif n2 == 0:
        total = n1 * n4
        total /= n3
        print(f'O resultado da regra de três é {total}.')
    elif n3 == 0:
        total = n1 * n4
        total /= n2
        print(f'O resultado da regra de três é {total}.')
    elif n4 == 0:
        total = n3 * n2
        total /= n1
        print(f'O resultado da regra de três é {total}.')
    #VENDO SE O USUÁRIO QUER CONTINUAR OU PARAR
    while continuar != 'S':
        continuar = str(input('Deseja continuar [S/N]: ')).upper()[0]
        if continuar in 'Ss':
            print('\n' * 10)
            continue
        elif continuar in 'Nn':
            print(('Encerrando programa...'))
            sleep(1.5)
            print('ENCERRADO!!!')
            break
        else:
            print('Digite novamente pois a letra/palavra digitado é inválido.')
    #VAI ENCERRAR O PROGRAMA POIS NO SEGUNDO WHILE SÓ ENCERRERÁ O SEGUNDO LAÇO
    if continuar == 'N':
        break
    #MUDANDO O VALOR DA VARIÁVEL PARA SER REPETIDA EM CADA LAÇO, TIRANDO ELE SÓ SE REPETI UMA VEZ POIS O VALOR PARA SAIR SERÁ ETERNO
    continuar = ''
