print('-----APLICANDO JUROS-----')
juros = taxa = tempo = capital = 0
while True:
    print('\n\n\nJ = C * I * T')
    print('TAXA EM MÊS, TEMPO EM MÊS\n')
    print('Se não tiver o valor, DIGITE 0')
    juros = float(input('Digite os juros do problema: '))
    taxa = float(input('Digite a taxa do problema: '))
    capital = float(input('Digite a capital do problema: '))
    tempo = float(input('Digite aqui o tempo dado pelo programa: '))
    #FIM DAS PERGUNTAS QUE RECEBERÃO OS DADOS
    #QUANDO O USUÁRIO NÃO TEM O VALOR
    if juros == 0:
        juros = capital * taxa * tempo
        print('Resultado: {:.2f}'.format(juros))
    elif capital == 0:
        apoio = taxa * tempo
        capital = apoio / juros
        print('Resultado: {:.2f}'.format(capital))
    elif taxa == 0:
        apoio = capital * tempo
        taxa = apoio / juros
        print('Resultado: {:.2f}'.format(taxa))
    elif tempo == 0:
        apoio = capital * taxa
        tempo = apoio / juros
        print('Resultado: {:.2f}'.format(tempo))
    else:
        print('Digitou um valor inválido, reiniciando o programa!!')
        continue
    #DECINDINDO SE IRÁ CONTINUAR OU ENCERRAR O PROGRAMA
    continuar = str(input('Você deseja continuar? [S/N]')).upper().strip()[0]
    if continuar in 'S':
        print('Reiniciando...')
        continue
    elif continuar in 'N':
        print('Encerrando...')
        break
