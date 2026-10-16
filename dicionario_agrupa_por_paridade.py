par_impar = {'par': [], 'impar': []}
lista = [1,2,3,4,5,6,7,8,9]
for numero in lista:
    if numero % 2 == 0:
        par_impar['par'].append(numero)
    else:
        par_impar['impar'].append(numero)
        
print(par_impar)