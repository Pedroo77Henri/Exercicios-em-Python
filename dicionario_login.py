usuarios = {
    "pedro": "1234",
    "admin": "admin123",
    "maria": "senha456",
    "joao": "abc123",
    "ana": "qwerty"
}
entrada1 = input('Digite o seu usuario: ')
if entrada1 in usuarios:
    senha = input(f'olá {entrada1} digite a sua senha: ')
    if senha == usuarios[entrada1]:
        print('Aecsso liberado')
    else:
        print('Senha incorreta')
else:
    print('Usuario Ivalido')
    

    


