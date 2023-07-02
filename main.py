import funcionalidades.verificacao as verificacao
import telas.Registrar_atestado as Registrar_atestado
import telas.tela_inicial as inicio


def main():
    opcao_escolhida = inicio.tela_inicial()
    if opcao_escolhida == "1":
        verificacao.limpar_tela()
        Registrar_atestado.registrar()
        return
    elif opcao_escolhida == "2":
        verificacao.limpar_tela()
        print("ok")
        return
    elif opcao_escolhida == "3":
        verificacao.limpar_tela()
        print("Obrigado por utilizar o Sistema ATEST-IFS. Até logo!")
        return

if __name__ == "__main__":
    verificacao.limpar_tela()
    main()
