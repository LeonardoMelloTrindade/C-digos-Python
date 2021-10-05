print('-----FATORIAL-----')
from time import sleep
num = int(input('Digite um número inteiro para exibir seu fatorial: '))
n = num
fatorial = 0
while n >= 2:
    if fatorial == 0:
        fatorial = n * (n - 1)
    elif fatorial != 0:
        fatorial = fatorial * (n - 1)
    n -= 1
print('Calculando...')
sleep(0.6)
print('A fatoração de {}! é {}.'.format(num, fatorial))
