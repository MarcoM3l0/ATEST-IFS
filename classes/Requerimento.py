import time
from datetime import date
import os
import os.path
import json
import cv2
from tkinter import Tk
from tkinter.filedialog import askopenfilename

import funcionalidades.verificacao as limpar
import telas.Registrar_atestado as registrar_atestado
import main as main

class Requerimento:
    def __init__(self, nome, curso, email, matricula, celular, justificativa_de_falat, segunda_chamada, exposicao_de_motivos, data_atestado, data_recebimento, assinatura):
        self.nome = nome
        self.curso = curso
        self.email = email
        self.matricula = matricula
        self.celular = celular
        self.justificativa_de_falta = justificativa_de_falat
        self.segunda_chamada = segunda_chamada
        self.exposicao_de_motivos = exposicao_de_motivos
        self.data_atestado = data_atestado
        self.data_recebimento = data_recebimento
        self.assinatura = assinatura

    def atestado_digitalizado(self):
        Tk().withdraw()  # Esconde a janela principal do Tkinter
        caminho_imagem = askopenfilename()
        imagem = cv2.imread(caminho_imagem) # pylint: disable=no-member
        self.atestado = imagem

def tela_registro_atestado(data):
    while True:
        print("         Registro de Atestado")
        print("===============================================")
        print("Por favor, preencha as informações abaixo:")

        nome = input("Nome: ")
        curso = input("Curso: ")
        email = input("Email: ")
        matricula = input("Matrícula: ")
        celular = input("Celular: ")

        limpar.limpar_tela()

        justificativa_de_falta = input("Justificativa de falta[S/N]: ")
        segunda_chamada = input("Segunda chamada [S/N]: ")

        limpar.limpar_tela()

        data_atestado = data
        data_recebimento = date.today()
        data_recebimento = data_recebimento.strftime('%d/%m/%Y')
        print(f"Data de recebimento: {data_recebimento}")
        assinatura = input("Assinatura: ")

        exposicao_de_motivos = input("Exposição de motivos: ")

        limpar.limpar_tela()
        
        # Função para carregar o atestado digitalizado
        def carregar_atestado():
            Tk().withdraw()  # Esconde a janela principal do Tkinter
            caminho_imagem = askopenfilename()
            imagem = cv2.imread(caminho_imagem) # pylint: disable=no-member
            return imagem

        # Chamada da função para carregar o atestado digitalizado
        print("Escolha o atestado")
        imagem_atestado = carregar_atestado() # Figurativo
        limpar.limpar_tela()

        # Criando uma instância do Requerimento com os dados fornecidos
        requerimento = Requerimento(
            nome,
            curso,
            email,
            matricula,
            celular,
            justificativa_de_falta,
            segunda_chamada,
            exposicao_de_motivos,
            data_atestado,
            data_recebimento,
            assinatura
        )

    
        # Diretório base do arquivo Python
        diretorio_base = os.path.dirname(os.path.abspath(__file__))


        # Convertendo o objeto Requerimento para um dicionário
        dados_requerimento = {
            "nome": requerimento.nome,
            "curso": requerimento.curso,
            "email": requerimento.email,
            "matricula": requerimento.matricula,
            "celular": requerimento.celular,
            "justificativa_de_falta": requerimento.justificativa_de_falta,
            "segunda_chamada": requerimento.segunda_chamada,
            "exposicao_de_motivos": requerimento.exposicao_de_motivos,
            "data_recebimento": requerimento.data_recebimento,
            "assinatura": requerimento.assinatura,
        }

        # Caminho para o arquivo JSON
        caminho_arquivo_json = os.path.join(diretorio_base, "..", "db", "requerimentos.json")

        # Verificar se o arquivo JSON já existe
        if os.path.isfile(caminho_arquivo_json):
            # Ler os dados existentes do arquivo JSON
            with open(caminho_arquivo_json, "r", encoding="utf-8") as arquivo_json:
                conteudo = arquivo_json.read()
                if conteudo:
                    conteudo_json = json.loads(conteudo)
                else:
                    conteudo_json = []
        else:
            conteudo_json = []

        # Adicionar o novo requerimento ao conteúdo existente
        conteudo_json.append(dados_requerimento)

        # Salvando os dados em um arquivo JSON
        with open(caminho_arquivo_json, "w", encoding="utf-8") as arquivo_json:
            json.dump(conteudo_json, arquivo_json)

        print("===============================================")
        print("      Atestado registrado com sucesso!")
        print("===============================================")

        while True:

            limpar.limpar_tela()

            opcao = input("Digite 's' para registrar outro atestado ou 'q' para voltar ao menu principal: ")

            if opcao.lower() == 'q' or opcao.lower() == 's':
                if opcao.lower() == 'q':
                    main.main()
                    return
                elif opcao.lower() == 's':
                    registrar_atestado.tela_registrar_atestado()
                    return

            limpar.limpar_tela()

            print("\033[91mErro: DIGITE APENAS  's' ou 'q'!\033[0m")
            time.sleep(0.5) # Aguarda meio segundo
            