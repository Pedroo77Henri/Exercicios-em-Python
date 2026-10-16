from enum import Enum

class RaridadeItema(Enum):
    comum = 1 
    raro = 2
    epico = 3
    lendario = 4


def recebe_informação():
    info = input('Digite o tipo de raridade do seu item: ')
    if hasattr(RaridadeItema, info):
        print(getattr(RaridadeItema, info).value)
    else:
        print('Esse atributo não existe')

if __name__ == "__main__":
    recebe_informação()

