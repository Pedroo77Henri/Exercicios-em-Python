while True:
    numero1 = input('Digite o primeiro numero para o calculo: ')
    numero2 = input('Digite o segundo numero para o calculo: ')

    if numero1.isdigit() and numero2.isdigit():
        numero1 = int(numero1)
        numero2 = int(numero2)
    else:
        print('Os valores não é inteiro')
        break
    
    condicao = input('Digite a operação logica que deseja fazer: *(multiplicação); /(Divisão); +(Soma); -(Subtração) ')
    if condicao == '*':
        multiplicacao = numero1*numero2
        print(f'Multiplicação = {multiplicacao}')
    elif condicao == '/':
        divisao = numero1/numero2
        print(f'Divisão = {divisao}')
    elif condicao == '+':
        soma = numero1+numero2
        print(f'Soma = {soma}')   
    elif condicao == '-':
        subtracao = numero1-numero2
        print(f'Subtração = {subtracao}')
    else:
        print('Operação logica invalida')    
    sair = input('Digite [s] para sair ou outro digito para continuar: ').lower().startswith('s')

    if sair is True:
        break