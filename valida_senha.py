while True:
    senha = input('Digite a sua senha: ')
    tamanho_senha = len(senha)
    if tamanho_senha < 6:
        print('Senha invalida')
        continue
    elif senha.isdigit():
        print('Senha invalida')
        continue
    elif not any(char.isalpha() for char in senha):
        print('Senha invalida')
        continue
    elif '' in senha:
        print('Senha invalida')
        continue
    else:
        print(f'Senha {senha} valida.')
        break