import funcionalidades.verificacao as verificar
import funcionalidades.registrar as opcoes_rig
import main
import classes.Requerimento as requerimento

def tela_registrar_atestado():
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
    while True:
        print(f'   Opeção - {opcao}')
        print("========================")
        print("Digite a data de emissão do Atestado(formato [DD/MM/AAAA]):")
        data = input("Data:")

        validado, dt_limite = verificar.validar_data(data)
        if validado and dt_limite == 0:
            return True, data
        
        if dt_limite == 1:
            main.main()
            return
        
        verificar.limpar_tela()

def registrar():
    opcao = tela_registrar_atestado()
    verificar.limpar_tela()

    if opcao == 'X':
        main.main()
        return
    
    prosseguir, data = verificar_data(opcao)

    if prosseguir:
        requerimento.tela_registro_atestado(data)
