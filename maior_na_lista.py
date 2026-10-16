def maior_que_dez(lista):
    for numero in lista:
        if numero >= 10:
            print(f'Os numeros maior que dez é {numero}')
    
    
lista = [1,2,3,4,10,20,30]
maior_que_dez(lista)    