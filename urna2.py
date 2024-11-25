import tkinter as tk
from tkinter import messagebox
import pickle
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

# Função para abrir urna e registrar votos
def abrir_urna(eleitor):
    def votar():
        voto = entrada_voto.get()
        if voto.isdigit():
            numero = int(voto)
            
            if numero == 0:  # Voto branco
                votos['branco'] = votos.get('branco', 0) + 1
                messagebox.showinfo("Sucesso", "Voto registrado como BRANCO")
            elif numero in candidatos:  # Voto válido
                candidatos[numero]['votos'] += 1
                salvar_dados(FILE_CANDIDATOS, candidatos)
                messagebox.showinfo("Sucesso", f"Voto registrado para: {candidatos[numero]['nome']}")
            else:  # Voto nulo
                votos['nulo'] = votos.get('nulo', 0) + 1
                messagebox.showinfo("Sucesso", "Voto registrado como NULO")
            
            salvar_dados(FILE_VOTOS, votos)
        else:
            messagebox.showwarning("Erro", "Digite um número válido.")
        
        urna_window.destroy()  # Fechar janela após votar

    urna_window = tk.Toplevel()
    urna_window.title("Urna Eletrônica")
    
    tk.Label(urna_window, text=f"Bem-vindo, {eleitor['nome']}!").pack(pady=10)
    tk.Label(urna_window, text="Digite o número do candidato ou 0 para Branco:").pack(pady=5)
    entrada_voto = tk.Entry(urna_window)
    entrada_voto.pack(pady=5)
    
    tk.Button(urna_window, text="Votar", command=votar).pack(pady=10)

# Função para registrar novos eleitores
def registrar_eleitor(titulo):
    def salvar():
        nome = entrada_nome.get()
        if nome:
            eleitores[titulo] = {'nome': nome}
            salvar_dados(FILE_ELEITORES, eleitores)
            messagebox.showinfo("Sucesso", f"Eleitor {nome} registrado com sucesso!")
            janela_registro.destroy()
        else:
            messagebox.showwarning("Erro", "Preencha o nome do eleitor.")

    janela_registro = tk.Toplevel()
    janela_registro.title("Registrar Novo Eleitor")
    
    tk.Label(janela_registro, text=f"Título de Eleitor: {titulo}").pack(pady=5)
    tk.Label(janela_registro, text="Nome do Eleitor:").pack(pady=5)
    entrada_nome = tk.Entry(janela_registro)
    entrada_nome.pack(pady=5)

    tk.Button(janela_registro, text="Registrar", command=salvar).pack(pady=10)

# Função para verificar título de eleitor
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

# Janela principal
root = tk.Tk()
root.title("Urna Eletrônica - Verificação de Título")
root.geometry("300x300")

tk.Label(root, text="Digite o título de eleitor:").pack(pady=10)
entrada_titulo = tk.Entry(root)
entrada_titulo.pack(pady=5)

tk.Button(root, text="Verificar", command=verificar_titulo).pack(pady=10)
tk.Button(root, text="Adicionar Candidato", command=adicionar_candidato).pack(pady=10)

root.mainloop()
