import tkinter as tk
from tkinter import messagebox
import pickle
from common import *
from eleicao import *
import os

FILE_ELEITORES = 'eleitores.pkl'
FILE_CANDIDATOS = 'candidatos.pkl'
FILE_VOTOS = 'votos.pkl'

# Funções para carregar e salvar dados em arquivos
def carregar_dados(nome_arquivo):
    if os.path.exists(nome_arquivo):
        with open(nome_arquivo, 'rb') as arquivo:
            return pickle.load(arquivo)
    return {}

def salvar_dados(nome_arquivo, dados):
    with open(nome_arquivo, 'wb') as arquivo:
        pickle.dump(dados, arquivo)

eleitores = carregar_dados(FILE_ELEITORES)
candidatos = carregar_dados(FILE_CANDIDATOS)
votos = carregar_dados(FILE_VOTOS)

# Função para adicionar candidatos
def adicionar_candidato():
    def salvar_candidato():
        numero = entrada_numero.get()
        nome = entrada_nome.get()

        if numero.isdigit() and nome:
            numero = int(numero)
            if numero in candidatos:
                messagebox.showwarning("Erro", "Número do candidato já existe.")
            else:
                candidatos[numero] = {'nome': nome, 'votos': 0}
                salvar_dados(FILE_CANDIDATOS, candidatos)
                messagebox.showinfo("Sucesso", f"Candidato {nome} adicionado com sucesso!")
                janela_adicionar.destroy()
        else:
            messagebox.showwarning("Erro", "Preencha todos os campos corretamente.")

    # Janela para registrar novo candidato
    janela_adicionar = tk.Toplevel()
    janela_adicionar.title("Adicionar Candidato")
    
    tk.Label(janela_adicionar, text="Número do Candidato:").pack(pady=5)
    entrada_numero = tk.Entry(janela_adicionar)
    entrada_numero.pack(pady=5)

    tk.Label(janela_adicionar, text="Nome do Candidato:").pack(pady=5)
    entrada_nome = tk.Entry(janela_adicionar)
    entrada_nome.pack(pady=5)

    tk.Button(janela_adicionar, text="Salvar", command=salvar_candidato).pack(pady=10)

# função para abrir urna e registrar votos
def abrir_urna(eleitor):
    def votar():
        voto = entrada_voto.get()
        if voto.isdigit():
            numero = int(voto)
            
            if numero == 0:  # Voto branco
                votos['branco'] = votos.get('branco', 0) + 1
                salvar_dados(FILE_VOTOS, votos)
                messagebox.showinfo("Sucesso", "Voto registrado como BRANCO")
            elif numero in candidatos:  # Voto válido
                candidatos[numero]['votos'] += 1
                salvar_dados(FILE_CANDIDATOS, candidatos)
                messagebox.showinfo("Sucesso", f"Voto registrado para: {candidatos[numero]['nome']}")
            else:  # Voto nulo
                votos['nulo'] = votos.get('nulo', 0) + 1
                salvar_dados(FILE_VOTOS, votos)
                messagebox.showinfo("Sucesso", "Voto registrado como NULO")
        else:
            messagebox.showwarning("Erro", "Digite um número válido.")
        
        urna_window.destroy()  # Fechar janela após votar

    urna_window = tk.Toplevel()
    urna_window.title("Urna Eletrônica")
    
    tk.Label(urna_window, text=f"Bem-vindo, {eleitor.nome}!").pack(pady=10)
    tk.Label(urna_window, text="Digite o número do candidato ou 0 para Branco:").pack(pady=5)
    entrada_voto = tk.Entry(urna_window)
    entrada_voto.pack(pady=5)
    
    tk.Button(urna_window, text="Votar", command=votar).pack(pady=10)

def carregar_eleitores():
    if os.path.exists("eleitores.pkl"):
        with open("eleitores.pkl", "rb") as arquivo:
            return pickle.load(arquivo)
    else:
        return {}

def salvar_eleitores(eleitores):
    with open("eleitores.pkl", "wb") as arquivo:
        pickle.dump(eleitores, arquivo)

def registrar_eleitor(titulo):
    def salvar():
        nome = entrada_nome.get()
        rg = entrada_rg.get()
        cpf = entrada_cpf.get()
        secao = entrada_secao.get()
        zona = entrada_zona.get()

        if nome and rg and cpf and secao and zona:
            eleitor = Eleitor(nome, rg, cpf, titulo, secao, zona)
            eleitores[titulo] = eleitor
            salvar_eleitores(eleitores)
    
            messagebox.showinfo("Sucesso", f"Eleitor {nome} registrado com sucesso!")
            janela_registro.destroy()
        else:
            messagebox.showwarning("Erro", "Todos os campos devem ser preenchidos.")

    janela_registro = tk.Toplevel()
    janela_registro.title("Registrar Novo Eleitor")
    
    tk.Label(janela_registro, text=f"Título de Eleitor: {titulo}").pack(pady=5)
    
    tk.Label(janela_registro, text="Nome do Eleitor:").pack(pady=5)
    entrada_nome = tk.Entry(janela_registro)
    entrada_nome.pack(pady=5)

    tk.Label(janela_registro, text="RG do Eleitor:").pack(pady=5)
    entrada_rg = tk.Entry(janela_registro)
    entrada_rg.pack(pady=5)

    tk.Label(janela_registro, text="CPF do Eleitor:").pack(pady=5)
    entrada_cpf = tk.Entry(janela_registro)
    entrada_cpf.pack(pady=5)

    tk.Label(janela_registro, text="Seção Eleitoral:").pack(pady=5)
    entrada_secao = tk.Entry(janela_registro)
    entrada_secao.pack(pady=5)

    tk.Label(janela_registro, text="Zona Eleitoral:").pack(pady=5)
    entrada_zona = tk.Entry(janela_registro)
    entrada_zona.pack(pady=5)

    tk.Button(janela_registro, text="Registrar", command=salvar).pack(pady=10)

def verificar_titulo():
    titulo = entrada_titulo.get()
    if titulo.isdigit():
        titulo = int(titulo)
        if titulo in eleitores:
            eleitor = eleitores[titulo]
            abrir_urna(eleitor)
        else:
            resposta = messagebox.askyesno("Título não encontrado", "Título não encontrado. Deseja registrar um novo eleitor?")
            if resposta:
                registrar_eleitor(titulo)
    else:
        messagebox.showwarning("Erro", "Digite um título válido.")

root = tk.Tk()
root.title("Urna Eletrônica - Verificação de Título")
root.geometry("300x300")

tk.Label(root, text="Digite o título de eleitor:").pack(pady=10)
entrada_titulo = tk.Entry(root)
entrada_titulo.pack(pady=5)

tk.Button(root, text="Verificar", command=verificar_titulo).pack(pady=10)
tk.Button(root, text="Adicionar Candidato", command=adicionar_candidato).pack(pady=10)


root.mainloop()
