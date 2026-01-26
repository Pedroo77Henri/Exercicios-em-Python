def tabuada(entrada):
    valores = [1,2,3,4,5,6,7,8,9,10]
    for digito in valores:
        digito *= entrada
        print(digito)
entrada = int(input('Digite um numero para ver sua tabuada '))
tabuada(entrada)