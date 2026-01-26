nome = input('Digite o seu nome: ')
tamanho = len(nome)
if tamanho < 4:
    print('Seu nome é pequeno')
elif tamanho >= 5 and tamanho <= 6:
    print('Seu nome é normal')
elif tamanho > 6:
    print('Seu nome é grande')
