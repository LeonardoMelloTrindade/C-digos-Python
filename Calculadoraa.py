print('-----CALCULADORA COM WHILE-----')
from time import sleep
import emoji
num1 = float(input('Digite o primeiro número: '))
num2 = float(input('Digite o segundo número: '))
operador = 0
#SO VAI ENCERRAR QUANDO O OPERADOR RECEBER O VALOR 5
while operador != 5:
    sleep(0.8)
    operador = int(input(('''Digite um número para realizar uma operação:
    [ 1 ] - Adição
    [ 2 ] - Multiplicação
    [ 3 ] - Maior e Menor
    [ 4 ] - Novos números
    [ 5 ] - Encerrar operação
    Qual o operador desejado? ''')))
    #ESTRUTURA DE REPETIÇÃO DOS OPERADORES
    #SOMAR
    if operador == 1:
        print('{:.2f} + {:.2f} = {:.2f}'.format(num1, num2, num1 + num2))
    #MULTIPLICAR
    elif operador == 2:
        print('{:.2f} x {:.2f} = {:.2f}'.format(num1, num2, num1 * num2))
    #MAIOR E MENOR NÚMERO
    elif operador == 3:
        if num1 > num2:
            print('{} é maior que {}.'.format(num1, num2))
        elif num2 > num1:
            print('{} é maior que o {}.'.format(num2, num1))
        elif num1 == num2:
            print('Ambos são iguais.')
        else:
            print('ERRO, TENTE NOVAMENTE!!!')
        #INSERIR NOVOS NÚMEROS
    elif operador == 4:
        num1 = float(input('Digite o primeiro número novamente: '))
        num2 = float(input('Digite o segundo número novamente: '))
    elif operador == 5:
        print(emoji.emojize("FIM DO PROGRAMA, OBRIGADO POR UTILIZAR :sparkling_heart: :sparkling_heart: :sparkling_heart:", use_aliases=True))
