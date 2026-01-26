def conta_pares(numero):
    acumulador = 0
    for digito in range(0, numero +1):
        if digito % 2 == 0:
            acumulador += 1
    return f'o numero digitado é {numero} e ele tem {acumulador} numeros pares.'
            

numero = int(input('Digite um numero: '))
print(conta_pares(numero))