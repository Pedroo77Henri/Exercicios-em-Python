alunos = {
    "João": [7.5, 8.0, 6.5],
    "José": [9.0, 8.5, 9.5],
    "Pedro": [6.0, 7.0, 5.5],
    "Felipe": [10.0, 9.5, 9.0],
    "Lucas": [8.0, 7.5, 8.5],
    "André": [6.5, 7.0, 6.0],
    "Bruno": [5.0, 6.0, 5.5]
}


ranking = []
for nome,notas in alunos.items():
    media = sum(notas) / len(notas)
    ranking.append((nome, media))

ranking.sort(key=lambda x: x[1], reverse=True)

for nome, media in ranking:
    print(f'A média do aluno {nome} é: {media:.2f}')