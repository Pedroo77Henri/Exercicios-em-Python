perguntas = [
    {
        'Pergunta': 'Quanto é 2+2?',
        'Opções': ['1', '3', '4', '5'],
        'Resposta': '4',
    },
    {
        'Pergunta': 'Quanto é 5*5?',
        'Opções': ['25', '55', '10', '51'],
        'Resposta': '25',
    },
    {
        'Pergunta': 'Quanto é 10/2?',
        'Opções': ['4', '5', '2', '1'],
        'Resposta': '5',
    },
]
respostas = 0
for dicionario in perguntas:
    print(dicionario['Pergunta'])
    for indice, valor in enumerate(dicionario['Opções']):
        print(f'{indice}) - {valor}')
    resposta_usuario = int(input('Escolha uma opção: '))
    if dicionario['Opções'][int(resposta_usuario)] == dicionario['Resposta']:
        print('Acertou')
        respostas +=1
    else:
        print('Incorreto')
if respostas == 3:
    print('Parabens você acertou as tres perguntas')
elif respostas == 2:
    print('Parabens você acertou duas e errou uma')
elif respostas == 1:
    print('Parabens você acertou uma e errou duas')    
else:
    print('Você errou todas')