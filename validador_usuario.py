import re
while True:
    padrao_valido = r'^[a-zA-Z0-9_]+$'
    usuario = input('Digite o seu usuario: ')
    tamanho_user = len(usuario)

    if tamanho_user < 6:
        print(f'Usuario {usuario} invalido, tem menos de 6 digitos')
        continue

    elif not any(char.isalpha() for char in usuario):
        print(f'Usuario {usuario} invalido, deve conter ao menos uma letra')
        continue

    elif usuario[:0].isdigit():
        print(f'Usuario {usuario} invalido, não pode começar com número')
        continue

    elif not re.match(padrao_valido, usuario):
        print(f'Usuario {usuario} invalido, não deve conter caracter especial')
        continue

    else:
        print(f'Usuario validado com sucesso {usuario}')