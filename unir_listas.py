arrays_1= ['Jhonatans', 'Maria', 'João']
arrays_2 = ['18', '16', '20']
resultado = [*arrays_1, *arrays_2]
resultado = [item for par in zip(arrays_1, arrays_2) for item in par]
print(resultado)