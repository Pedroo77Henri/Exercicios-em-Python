lista = [1, 2, 3, 4, 5]

while True:
    opcao = input('Digite um numero para 1-incluir na lista, 2-apagar item na lista, 3-listar valores da lista, 4-sair: ')

    if not opcao.isdigit():
        print('O valor digitado não é um número.')
        continue

    opcao = int(opcao)

    if opcao == 1:
        adicionar = int(input('Digite um valor para adicionar na lista: '))
        lista.append(adicionar)

    elif opcao == 2:
        apagar = int(input('Digite o valor que deseja apagar da lista: '))
        if apagar in lista:
            lista.remove(apagar)
        else:
            print('Valor não encontrado na lista.')

    elif opcao == 3:
        print(f'Listando valores da lista: {lista}')

    elif opcao == 4:
        print('Saindo...')
        break

    else:
        print('Valor inválido.')
