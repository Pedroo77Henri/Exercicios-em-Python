def soma_lista(lista):
    soma = 0
    for numero in lista:
        soma += numero
    return soma
numeros = [1, 2, 3, 4, 5]
resultado = soma_lista(numeros)
