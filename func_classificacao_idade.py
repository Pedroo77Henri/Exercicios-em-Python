def classificacao_idade(idade):
    if idade <= 12:
        return f'{idade} anos, criança'
    elif idade >=13 and idade <= 17:
        return f'{idade} anos, adolescente'
    if idade >= 18:
        return f'{idade} anos, adulto'
    
idade = int(input('Digite sua idade '))
print(classificacao_idade(idade))