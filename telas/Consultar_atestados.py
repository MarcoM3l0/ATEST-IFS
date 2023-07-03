import funcionalidades.verificacao as limpar
import funcionalidades.consultar as consulta
import main

def consultar_atestados():
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