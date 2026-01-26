print('Bem-vindo ao cadastro de nomes!')
nomes = []
while True:
    opcao = input('Digite para dar continuidade: 1 → Adicionar um nome; 2 → Remover um nome; 3 → Listar os nomes; 4 → Sair:  ')
    if opcao == '1':
        nome = input('Nome que deseja adicionar: ')
        if any(char.isdigit() for char in nome):
            print('Não pode ter numeros')
        else:
            nomes.append(nome)
            print(f'Nome {nome} adicionado')
    elif opcao == '2':
        remover = input('Digite o nome que deseja remover: ')
        try:
            nomes.remove(remover)
            print(f'Nome {remover} removido')
        except:
            print(f'{remover} não se encontra na lista')
    elif opcao == '3':
        print(f'listando {nomes}')
    else:
        print('Saindo')
        break
