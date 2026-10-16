import copy
produtos = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.90},
]


def aumentar_precos(lista_original):
 
    nova_lista = copy.deepcopy(lista_original)
    for produto in nova_lista:
   
        produto['preco'] = produto['preco'] * (1.1)
        ordena_produto = sorted(produtos['nome'])

    return nova_lista, ordena_produto


novos_produtos = aumentar_precos(produtos)

print("Original:", produtos)
print("Novos (10% mais caros):", novos_produtos)