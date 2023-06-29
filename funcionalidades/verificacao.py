import time
import os
from datetime import datetime, timedelta
    
def limpar_tela():
    # Limpar o terminal/console
    if os.name in ('nt', 'dos', 'ce'):  # Para Windows
        os.system('cls')

def verificar_tela_inicial(opcao):
    if opcao == "1":
        return True
    elif opcao == "2":
        return True
    elif opcao == "3":
        return True
    
    print("\033[91mOpção inválida. Por favor, escolha uma opção válida.\033[0m")
    time.sleep(0.5) # Aguarda meio segundo
    return False

def verificar_algarismo_registrar(opcao):
    algarismo = ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX', 'X']

    if (opcao in algarismo):
        return True
    
    print("\033[91mOpção inválida. Por favor, escolha uma opção válida.\033[0m")
    time.sleep(0.5) # Aguarda meio segundo
    return False

def validar_data(data_str):
    # Converter a string da data para um objeto datetime
    try:
        data = datetime.strptime(data_str, "%d/%m/%Y")
    except ValueError:
        print("\033[91mErro: formatação errada digite de novo\033[0m")
        time.sleep(0.5) # Aguarda meio segundo
        return False
    
    # Obter a data atual
    data_atual = datetime.now().date()
    
    # Verificar se já se passaram cinco dias
    diferenca = data_atual - data.date()
    if diferenca > timedelta(days=5):
        print("\033[91mJá se passaram cinco dias desde a data inserida.\033[0m")
        print("\033[91m Capítulo IV - § 3° A solicitação de justificativa de falta deverá ser realizada em até 5 dias corritos (...) \033[0m")
        time.sleep(2) # Aguarda 2 segundos
        return False
    else:
        return True