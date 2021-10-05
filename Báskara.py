print('-----BÁSKARA-----')
from math import pow, sqrt
print('A estrutura inicial é nx² + nx + n = 0')
a = int(input('Digite o primeiro valor: '))
b = int(input('Digite o segundo valor: '))
c = int(input('Digite o terceiro valor: '))
print(f'{a}x² + {b}x + {c} = 0')
#ACHANDO O DELTA
delta = pow(b, 2) - (4 * a * c)
#Achando a primeira raiz
x1 = (-b + sqrt(delta)) / (2 * a)
#Achando a segunda raiz
x2 = (-b - sqrt(delta)) / (2 * a)
#VERIFICANDO O VALOR DO DELTA
print('\n' * 20)
if delta < 0:
    print(f'Delta vale {delta:.2f}')
    print('Não existe raiz com delta negativo.')
elif delta == 0:
    print(f'Delta vale {delta:.2f}')
    print(f'o única raiz é: {x1:.2f}')
else:
    print(f'Delta vale {delta:.2f}')
    print(f'A primeira raiz vale: {x1:.2f}')
    print(f'A segunda raiz vale: {x2:.2f}')
