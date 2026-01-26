email_usuario = input('Digite o seu e-mail: ')
email_usuario = email_usuario.strip()
if email_usuario.count('@') != 1:
    print('E-mail invalido')
posicao_arroba = email_usuario.index('@')
if posicao_arroba == 0:
    print('E-mail invalido')
verifica_arroba = email_usuario[posicao_arroba + 1:]
if verifica_arroba == '':
    print('E-mail invalido')
if verifica_arroba.count('.') == 0:
    print('E-mail invalido')
else:
    print(f'E-mail {email_usuario} valido.')

