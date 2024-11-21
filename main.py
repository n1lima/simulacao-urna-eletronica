import pickle
import traceback
import gerenciar_urna
from common import *
from tkinter import *

FILE_ELEITORES = 'eleitores.pkl'
FILE_CANDIDATOS = 'candidatos.pkl'

def menu(opcao):
    opcoes = {
        1: "1-Novo Eleitor",
        2: "2-Atualizar Eleitor",
        3: "3-Inserir Candidato",
        4: "4-Listar Candidatos",
        5: "5-Iniciar Urna",
        6: "6-Testar Urna",
        7: "7-Emitir Zeresima",
        8: "8-Finalizar"
    }
    print(opcoes.get(opcao, "Opção inválida"))

def inserir_eleitor(eleitores):
    titulo = int(input("Digite o Títlulo: "))

    if titulo in eleitores:
        raise Exception("Titulo já existente!")

    nome = input("Digite o nome: ")
    RG = input("Digite o RG: ")
    CPF = input("Digite o CPF: ")
    secao = int(input("Digite a secao: "))
    zona = int(input("Digite a zona: "))

    eleitor = Eleitor(nome, RG, CPF, titulo, secao, zona)
    eleitores[eleitor.get_titulo()] = eleitor

    with open(FILE_ELEITORES, 'wb') as arquivo:
        pickle.dump(eleitores, arquivo)

    print('Eleitor gravado com sucesso!')
    print(eleitor)

def atualizar_eleitor(eleitores):
    titulo = int(input('Digite o titulo do eleitor: '))

    if titulo in eleitores:
        eleitor = eleitores[titulo]
        print(eleitor)
        secao = int(input("Digite a nova secao: "))
        zona = int(input("Digite a nova zona: "))
        eleitor.secao = secao
        eleitor.zona = zona

        with open(FILE_ELEITORES, 'wb') as arquivo:
            pickle.dump(eleitores, arquivo)

        print('Atualizados dados do eleitor!')
        print(eleitor)
    else:
        raise Exception('Titulo inexistente')

def inserir_candidato(candidatos):
    numero = int(input("Digite o número do candidato: "))

    if numero in candidatos:
        raise Exception("Candidato já existente!")

    nome = input("Digite o nome: ")
    RG = input("Digite o RG: ")
    CPF = input("Digite o CPF: ")

    candidato = Candidato(nome, RG, CPF, numero)
    candidatos[candidato.get_numero()] = candidato

    with open(FILE_CANDIDATOS, 'wb') as arquivo:
        pickle.dump(candidatos, arquivo)

    print('Candidato gravado com sucesso!')
    print(candidato)

def listar_candidatos(candidatos):
    for candidato in candidatos.values():
        print(candidato)

janela = Tk()
janela.title('Urna Eletrônica')
janela.geometry("300x400")

# Adicionando o texto de boas-vindas
texto_bem_vindo = Label(janela, text="Bem-vindo à Urna Eletrônica", font=("Arial", 14), pady=10)
texto_bem_vindo.pack()

# Adicionando os botões do menu
botoes = [
    ("Novo Eleitor", 1),
    ("Atualizar Eleitor", 2),
    ("Inserir Candidato", 3),
    ("Listar Candidatos", 4),
    ("Iniciar Urna", 5),
    ("Testar Urna", 6),
    ("Emitir Zeresima", 7),
    ("Finalizar", 8)
]

for texto, opcao in botoes:
    botao = Button(janela, text=texto, command=lambda op=opcao: menu(op), width=20)
    botao.pack(pady=5)

janela.mainloop()
