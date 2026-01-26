def maior_entre(numero1, numero2):
    if numero1 > numero2:
        return f'numero 1 é maior que numero 2'
    elif numero2 > numero1:
        return f'numero 2 é maior que numero 1'
    else:
        return 'Valores iguais'
    
while True:
    try:
        numero1 = int(input('Digite o numero 1 '))
        numero2 = int(input('Digite o numero 2 '))
        print(maior_entre(numero1, numero2))
        break
    except:
        print('Valor digitado não é um numero.')