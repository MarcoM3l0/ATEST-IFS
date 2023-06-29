import json
import os

def exibir_opcoe():
    # Diretório base do arquivo Python
    diretorio_base = os.path.dirname(os.path.abspath(__file__))
    
    # Caminho para o arquivo JSON
    caminho_arquivo_json = os.path.join(diretorio_base, "..", "db", "doc_aceitos.json")

    # Leitura do arquivo JSON
    with open(caminho_arquivo_json, encoding="utf-8") as file:
        opcoes_atestados = json.load(file)

    # Exibição das opções
    for chave, opcao in opcoes_atestados.items():
        print(f"{chave}. {opcao}")

