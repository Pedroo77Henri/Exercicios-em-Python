import json

lista = []

def opcoes():
    while True:
        opcao = input('Digite uma opção: 1 add tarefa; 2 listar; 3 remover; 4 sair: ')
        
        if opcao == '1':
            adicionar_tarefa()
        elif opcao == '2':
            listar_tarefa()
        elif opcao == '3':
            remover_tarefa()
        elif opcao == '4':
            break
        else:
            print('Opção inválida')

def salvar_tarefas():
    with open("tarefas.json", "w") as arquivo:
        json.dump(lista, arquivo)

def carregar_tarefas():
    global lista
    try:
        with open("tarefas.json", "r") as arquivo:
            lista = json.load(arquivo)
    except FileNotFoundError:
        lista = []

def adicionar_tarefa():
    tarefa = input('Digite a tarefa que deseja adicionar: ')
    lista.append(tarefa)
    salvar_tarefas()
    print('Tarefa adicionada!')

def listar_tarefa():
    if lista:
        print("\nLista de tarefas:")
        for i, tarefa in enumerate(lista, 1):
            print(f"{i}. {tarefa}")
    else:
        print("Nenhuma tarefa cadastrada.")

def remover_tarefa():
    retirar_da_lista = input('Digite a tarefa que deseja remover: ')
    
    if retirar_da_lista in lista:
        lista.remove(retirar_da_lista)
        salvar_tarefas()
        print('Removido!')
    else:
        print('Tarefa não encontrada')

carregar_tarefas()
opcoes()