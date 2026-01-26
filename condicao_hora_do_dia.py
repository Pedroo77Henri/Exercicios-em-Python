horas = int(input('Digite o horario: '))

if horas <= 11:
    print(f'Bom dia, são {horas} horas')
elif horas <= 17:
    print(f'Boa tarde, são {horas} horas')
elif horas >= 18:
    print(f'Boa noite, são {horas} horas')
else:
    print('Valor invalido')