import json
import os

def consultar_atestados_por_matricula(matricula):
    """
    Consulta os atestados de um determinado aluno por matrícula.

    Parâmetros:
        - matricula (str): Matrícula do aluno a ser consultada.

    Retorna:
        Uma lista contendo os atestados encontrados para a matrícula especificada.

    """

    # Diretório base do arquivo Python
    diretorio_base = os.path.dirname(os.path.abspath(__file__))

    # Caminho para o arquivo JSON
    caminho_arquivo_json = os.path.join(diretorio_base, "..", "db", "requerimentos.json")

    with open(caminho_arquivo_json, encoding='utf-8') as arquivo:
        dados = json.load(arquivo)

    atestados_encontrados = []
    for atestado in dados:
        if atestado["matricula"] == str(matricula):
            atestados_encontrados.append(atestado)

    return atestados_encontrados

def cunsultar(matricula_desejada):
    """
    Consulta os atestados de um determinado aluno e exibe os resultados.

    Parâmetros:
        - matricula_desejada (str ou int): Matrícula do aluno a ser consultada.

    Retorna:
        - False: Caso o usuário digite 'q' para voltar ao menu principal.
        - True: Caso o usuário digite 's' para procurar outro atestado.

    """

    resultados = consultar_atestados_por_matricula(matricula_desejada)
    return exibir_os_resultados(resultados, matricula_desejada)

def exibir_os_resultados(resultados, matricula_desejada):
    """
    Exibe os resultados da consulta dos atestados de um aluno.

    Parâmetros:
        - resultados (list): Lista contendo os atestados encontrados.
        - matricula_desejada (str ou int): Matrícula do aluno consultado.

    """
    
    if resultados:
        print("Atestados encontrados para a matrícula", matricula_desejada + ":")
        for atestado in resultados:
            print("Nome:", atestado["nome"])
            print("Curso:", atestado["curso"])
            print("Email:", atestado["email"])
            print("Matrícula:", atestado["matricula"])
            print("Celular:", atestado["celular"])
            print("Justificativa de falta:", atestado["justificativa_de_falta"])
            print("Segunda chamada:", atestado["segunda_chamada"])
            print("Exposição de motivos:", atestado["exposicao_de_motivos"])
            print("Data de recebimento:", atestado["data_recebimento"])
            print("Assinatura:", atestado["assinatura"])
            print("----------------------------------")
    else:
        print("Nenhum atestado encontrado para a matrícula", matricula_desejada)

    while True:

            opcao = input("Digite 's' para procura outro atestado ou 'q' para voltar ao menu principal: ")

            if opcao.lower() == 'q' or opcao.lower() == 's':
                if opcao.lower() == 'q':
                    return False
                elif opcao.lower() == 's':
                    return True
