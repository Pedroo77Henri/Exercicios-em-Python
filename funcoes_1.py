def multiplica_numeros (*args):
    resultado = 1
    for digito in args:
        resultado *= digito
    return resultado
print(multiplica_numeros(1, 2, 3, 4, 5))

def impar_par():
    numero = input('Digite um numero: ')
    numero = int(numero)
    if numero % 2 == 0:
        return f'Numero {numero} é par'
    else:
        return f'O número {numero} é impar'
print(impar_par())

