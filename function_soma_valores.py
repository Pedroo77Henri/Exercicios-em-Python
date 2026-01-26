def soma_valores(numero):
    acumulador = 0 
    for digito in range(1, numero + 1):
        acumulador += digito
    return acumulador
    
numero = int(input('Digite um numero '))
resultado = soma_valores(numero)
print(f'A soma dos números de 1 até {numero} é {resultado}')



