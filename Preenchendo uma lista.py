print('FAZ PARTE')
numero = list()
digitado = 0
while True:
    digitado = int(input('Digite algum número: '))
    if digitado not in numero:
        numero.append(digitado)
        print('Valor adicionado...')
    else:
        print('Valor já digitado, digite outro valor ou encerre o programa.')
    desejo = str(input('Você deseja continuar [S/N]: '))
    if desejo in 'Ss':
        continue
    elif desejo in 'Nn':
        print('OK! Encerrando o programa...')
        break
numero.sort()
print(f'O valores adicionados: {numero}')