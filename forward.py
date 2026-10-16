class Inventario:
    def __init__(self):
        self.itens = []

    def adicionar_item(self, item: "Item"):
        self.itens.append(item)
        item.inventario = self


class Item:
    def __init__(self, nome, peso, valor):
        self.nome = nome
        self.peso = peso
        self.valor = valor
        self.inventario: "Inventario | None" = None

inventario = Inventario()

espada = Item("Espada", 7, 100)
escudo = Item("Escudo", 10, 150)
pocao = Item("Poção", 1, 50)

inventario.adicionar_item(espada)
inventario.adicionar_item(escudo)
inventario.adicionar_item(pocao)

print(espada.inventario)
print(inventario.itens)