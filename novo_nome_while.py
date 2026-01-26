# Exemplo de iteração (percorrer) uma string usando while

# A string que queremos percorrer
nome = 'Maria Helena'  # Cada letra tem um índice (posição): 0, 1, 2, ...

# Variável que vai controlar em qual posição (índice) estamos na string
indice = 0

# Variável que vai guardar o novo nome com os asteriscos
novo_nome = ''

# Enquanto o índice for menor que o tamanho total da string 'nome'
while indice < len(nome):
    # Pega a letra atual de acordo com o índice
    letra = nome[indice]
    
    # Adiciona um asterisco e a letra na nova string
    # Exemplo: se letra for 'M', adiciona '*M' em novo_nome
    novo_nome += f'*{letra}'
    
    # Avança o índice para ir para a próxima letra
    indice += 1

# Depois que o loop termina, adiciona um último asterisco no final
novo_nome += '*'

# Mostra o resultado final na tela
print(novo_nome)
