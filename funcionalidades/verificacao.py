import time
import os
from datetime import datetime, timedelta
    
def limpar_tela():
    """
    Limpa o terminal ou console.

    Esta função verifica o sistema operacional e utiliza o comando adequado para limpar o terminal/console.
    """

    if os.name in ('nt', 'dos', 'ce'):  # Para Windows
        os.system('cls')

def verificar_tela_inicial(opcao):
    """
    Verifica se a opção da tela inicial é válida.

    Parâmetros:
    - opcao (str): A opção selecionada pelo usuário.

    Retorna:
    - True se a opção for válida.
    - False se a opção for inválida.

    A função verifica se a opção selecionada pelo usuário é uma opção válida. Se for válida, retorna True.
    Caso contrário, imprime uma mensagem de erro, espera meio segundo e retorna False.
    """

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
    """
    Verifica se a opção de algarismo para registrar é válida.

    Parâmetros:
    - opcao (str): A opção de algarismo selecionada pelo usuário.

    Retorna:
    - True se a opção for válida.
    - False se a opção for inválida.

    A função verifica se a opção selecionada pelo usuário é um algarismo válido. Se for válido, retorna True.
    Caso contrário, imprime uma mensagem de erro, espera meio segundo e retorna False.
    """

    algarismo = ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX', 'X']

    if (opcao in algarismo):
        return True
    
    print("\033[91mOpção inválida. Por favor, escolha uma opção válida.\033[0m")
    time.sleep(0.5) # Aguarda meio segundo
    return False

def validar_data(data_str):
    """
    Valida a data inserida pelo usuário.

    Parâmetros:
    - data_str (str): A data inserida pelo usuário.

    Retorna:
    - Uma tupla contendo:
        - True se a data for válida.
        - False se a data for inválida.
        - 0 se a data for válida e dentro do período permitido.
        - 1 se a data for válida, mas já se passaram mais de cinco dias.

    A função verifica se a data inserida pelo usuário está no formato correto (%d/%m/%Y) e é uma data válida.
    Em seguida, compara a data inserida com a data atual e verifica se já se passaram mais de cinco dias.
    Retorna True se a data for válida e dentro do período permitido.
    Caso contrário, imprime uma mensagem de erro apropriada, aguarda o tempo necessário e retorna False junto com um código de status.
    """
    
    # Converter a string da data para um objeto datetime
    try:
        data = datetime.strptime(data_str, "%d/%m/%Y")
    except ValueError:
        print("\033[91mErro: formatação errada digite de novo\033[0m")
        time.sleep(0.5) # Aguarda meio segundo
        return False, 0
    
    # Obter a data atual
    data_atual = datetime.now().date()
    
    # Verificar se já se passaram cinco dias
    diferenca = data_atual - data.date()
    if diferenca > timedelta(days=5):
        print("\033[91mJá se passaram cinco dias desde a data inserida.\033[0m")
        print("\033[91m Capítulo IV - § 3° A solicitação de justificativa de falta deverá ser realizada em até 5 dias corritos (...) \033[0m")
        time.sleep(3) # Aguarda 2 segundos
        return False, 1
    else:
        return True, 0