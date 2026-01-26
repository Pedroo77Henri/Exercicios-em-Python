numero_secreto = 20
tentativas = 0
while True:
    chute = input('Dgitie um número para tentar advinhar o número secreto: ')
    tentativas += 1
    if not chute.isdigit():
        print('O valor digitado não é um numero!')
        continue
    chute = int(chute)
    if chute > numero_secreto:
        print('O numero secreto é menor')
    elif chute < numero_secreto:
        print('O numero secreto é maior')
    else:
        print(f'Parabens voce acertou o numero secreto {numero_secreto} com {tentativas} tentativas ')
        break