import funcionalidades.verificacao as limpar
import funcionalidades.consultar as consulta
import main

def consultar_atestados():
    """
    Função responsável por permitir a consulta de atestados médicos.

    Esta função solicita ao usuário uma matrícula e consulta os atestados médicos associados a essa matrícula.
    O resultado da consulta é exibido na tela.

    Returns:
        None
    """
    while True:  
        print("  Consulta de Atestados")
        print("=========================")
        print("Digite a matrícula para consultar os atestados: ")
        matricula_desejada = input("matrícula: ")

        limpar.limpar_tela()

        respota = consulta.cunsultar(matricula_desejada)
        
        limpar.limpar_tela()

        if not respota:
            main.main()
            return