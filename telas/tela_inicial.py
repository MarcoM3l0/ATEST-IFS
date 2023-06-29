import funcionalidades.verificacao as verificacao

def tela_inicial():
    while True:
        print("         Bem-vindo ao ATEST-IFS")
        print("===============================================")
        print("         Por favor, escolha uma opção:")
        print("         1. Registrar novo atestado")
        print("         2. Consultar atestados recebidos")
        print("         3. Sair")
        print("===============================================")

        opcao = input("Digite o número da opção desejada: ")
        validado = verificacao.verificar_tela_inicial(opcao)
        if validado:
            return opcao

        verificacao.limpar_tela()