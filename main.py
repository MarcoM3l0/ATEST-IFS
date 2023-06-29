import funcionalidades.verificacao as verificacao
import telas.Registrar_atestado as Registrar_atestado

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

def main():
    opcao_escolhida = tela_inicial()
    if opcao_escolhida == "1":
        verificacao.limpar_tela()
        Registrar_atestado.registrar()
    elif opcao_escolhida == "2":
        verificacao.limpar_tela()
        print("ok")
    elif opcao_escolhida == "3":
        verificacao.limpar_tela()
        print("Obrigado por utilizar o Sistema ATEST-IFS. Até logo!")

if __name__ == "__main__":
    verificacao.limpar_tela()
    main()
