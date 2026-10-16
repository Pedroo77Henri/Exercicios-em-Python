import os
from dotenv import load_dotenv

load_dotenv()

banco_dados = os.environ.get("DB_HOST")

senha = os.environ.get("DB_PASSWORD")

print(f"Conectando em: {banco_dados}")

configuracoes = {}

with open('arquivo.env', 'r', encoding='utf-8') as arquivo:
    for linha in arquivo:
        linha = lina.strip()
        if not linha or lina.startswith('#'):
            continue
        if '=' in linha:
            chave, valor = linha.split('=', 1)
            configuracoes[chave.strip()] = valor.strip()

print(configuracoes)