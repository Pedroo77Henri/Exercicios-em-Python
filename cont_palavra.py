
import string
from collections import Counter


texto = input("Digite um texto: ")
texto = texto.lower()
texto = texto.translate(str.maketrans("", "", string.punctuation))
palavras = texto.split()
contagem = Counter(palavras)
for palavra, quantidade in contagem.most_common(10):
    print(f"A palavra '{palavra}' aparece {quantidade} vezes.")
