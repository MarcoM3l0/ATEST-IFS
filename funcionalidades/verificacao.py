import time
import os
    
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
    time.sleep(0.5) # Aguarda 1 segundos
    return False

def verificar_algarismo_registrar(opcao):
    algarismo = ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX', 'X']

    if (opcao in algarismo):
        return True
    
    print("\033[91mOpção inválida. Por favor, escolha uma opção válida.\033[0m")
    time.sleep(0.5) # Aguarda 1 segundos
    return False