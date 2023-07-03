import funcionalidades.verificacao as verificacao

def tela_inicial():

    """
    Exibe a tela inicial do aplicativo ATEST-IFS e permite ao usuário selecionar uma opção.

    Retorna:
    - A opção selecionada pelo usuário.

    Comportamento:
    - Exibe o cabeçalho do aplicativo.
    - Exibe as opções disponíveis.
    - Solicita ao usuário que digite o número da opção desejada.
    - Chama a função 'verificar_tela_inicial' para validar a opção digitada.
    - Se a opção for válida, retorna o valor.
    - Se a opção for inválida, exibe uma mensagem de erro e solicita uma nova entrada.
    - Chama a função 'limpar_tela' para limpar a tela antes de retornar.
    """

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