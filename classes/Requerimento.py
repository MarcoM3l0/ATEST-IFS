import cv2
from tkinter import Tk
from tkinter.filedialog import askopenfilename

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
        self.imagem = imagem

from tkinter import Tk
from tkinter.filedialog import askopenfilename
import cv2

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

        justificativa_de_falta = input("Justificativa de falta: ")
        segunda_chamada = input("Segunda chamada: ")

        data_atestado = data
        data_recebimento = input("Data de recebimento: ")
        assinatura = input("Assinatura: ")

        exposicao_de_motivos = input("Exposição de motivos: ")

        # Função para carregar o atestado digitalizado
        def carregar_atestado():
            Tk().withdraw()  # Esconde a janela principal do Tkinter
            caminho_imagem = askopenfilename()
            imagem = cv2.imread(caminho_imagem) # pylint: disable=no-member
            return imagem

        # Chamada da função para carregar o atestado digitalizado
        imagem_atestado = carregar_atestado()

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
        requerimento.imagem = imagem_atestado

        print("===============================================")
        print("Atestado registrado com sucesso!")
        print("===============================================")

        opcao = input("Digite 's' para registrar outro atestado ou 'q' para voltar ao menu principal: ")
        if opcao.lower() == 'q':
            return
