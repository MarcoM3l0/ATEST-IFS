import funcionalidades.verificacao as verificar
import funcionalidades.registrar as opcoes_rig
import main
import classes.Requerimento as requerimento

def tela_registrar_atestado():
    """
    Exibe a tela de registro de novo atestado e solicita a seleção do tipo do atestado.

    Returns:
        str: O tipo do atestado selecionado.
    """
    while True:
        print("Registro de Novo Atestado")
        print("========================")

        opcoes_rig.exibir_opcoe()

        print("========================")
        print("Selecione o tipo do atestado (o algarismo correspondente):")

        opcao = input("Opção: ").upper().strip()

        validado = verificar.verificar_algarismo_registrar(opcao)
        if validado:
            return opcao

        verificar.limpar_tela()

def verificar_data(opcao):
    """
    Verifica a validade da data de emissão do atestado.

    Args:
        opcao (str): O tipo do atestado selecionado.

    Returns:
        tuple: Uma tupla contendo um valor booleano indicando se a data é válida e a data de emissão.
    """
    while True:
        print(f'   Opção - {opcao}')
        print("========================")
        print("Digite a data de emissão do Atestado(formato [DD/MM/AAAA]):")
        data = input("Data:")

        verificar.limpar_tela()

        validado, dt_limite = verificar.validar_data(data)
        if validado and dt_limite == 0:
            return True, data
        
        if not validado and dt_limite == 1:
            verificar.limpar_tela()
            main.main()
            return False, data
        
        verificar.limpar_tela()

def registrar():
    """
    Função principal para o registro de atestados.

    Essa função realiza o registro de um novo atestado, exibindo a tela de registro,
    solicitando o tipo do atestado e verificando a validade da data de emissão.

    Retorna:
        None
    """
    opcao = tela_registrar_atestado()
    verificar.limpar_tela()

    if opcao == 'X':
        main.main()
        return
    
    prosseguir, data = verificar_data(opcao)

    verificar.limpar_tela()

    if prosseguir:
        requerimento.tela_registro_atestado(data)
