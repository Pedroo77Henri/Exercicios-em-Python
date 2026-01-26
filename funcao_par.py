def par_ou_impar(numero):
    if numero % 2 == 0:
        return f'{numero} é Par'
    else:
        return f'{numero} é Impar'

while True:
    try:
        entrada = int(input('Digite um numero: '))
        print(par_ou_impar(entrada))
        break
    except:
        print('Valor informado não é um numero.')