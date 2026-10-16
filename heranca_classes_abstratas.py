from abc import ABC, abstractmethod

class Personagem(ABC):
    def __init__(self, nome, vida):
        self.nome = nome
        self.vida = vida

    @abstractmethod
    def ataque(self):
        pass
    @abstractmethod
    def defesa(self):
        pass

class Guerreiro(Personagem):
    def ataque(self):
        print('Todos eles tem uma espada')
    
    def defesa(self):
        print('Todos eles tem um escudo')

class Mago(Personagem):
    def ataque(self):
        print('Todos eles tem uma vara magica')
    
    def defesa(self):
        print('Todos eles tem uma capa protetora')


usuario = Mago('Nome: Mago Ungry', 'Vida: 100')
print(usuario.nome)
print(usuario.vida)
usuario.ataque()
usuario.defesa()

