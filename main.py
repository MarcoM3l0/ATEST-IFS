import funcionalidades.verificacao as verificacao
import telas.Registrar_atestado as Registrar_atestado
import telas.tela_inicial as inicio
import telas.Consultar_atestados as consulta


def main():

    """
    Função principal que controla o fluxo do aplicativo.

    A função exibe a tela inicial do aplicativo, verifica a opção escolhida pelo usuário e chama as funcionalidades
    correspondentes com base na escolha.

    :return: None
    """

    opcao_escolhida = inicio.tela_inicial()
    if opcao_escolhida == "1":
        verificacao.limpar_tela()
        Registrar_atestado.registrar()
        return
    elif opcao_escolhida == "2":
        verificacao.limpar_tela()
        consulta.consultar_atestados()
        return
    elif opcao_escolhida == "3":
        verificacao.limpar_tela()
        print("Obrigado por utilizar o Sistema ATEST-IFS. Até logo!")
        return

if __name__ == "__main__":
    verificacao.limpar_tela()
    main()
