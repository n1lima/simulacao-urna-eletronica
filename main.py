import tkinter as tk
from tkinter import messagebox
import pickle
from common import Eleitor, Candidato
from eleicao import Urna
import os

FILE_ELEITORES = 'eleitores.pkl'
FILE_CANDIDATOS = 'candidatos.pkl'

def carregar_eleitores():
    try:
        with open(FILE_ELEITORES, 'rb') as arquivo:
            return pickle.load(arquivo)
    except FileNotFoundError:
        return {}

def salvar_eleitores(eleitores):
    with open(FILE_ELEITORES, 'wb') as arquivo:
        pickle.dump(eleitores, arquivo)

def carregar_candidatos():
    try:
        with open(FILE_CANDIDATOS, 'rb') as arquivo:
            return pickle.load(arquivo)
    except FileNotFoundError:
        return {}

eleitores = carregar_eleitores()
candidatos = carregar_candidatos()

def abrir_urna(eleitor):
    def votar():
        voto = entrada_voto.get()  
        if voto.isdigit(): 
            numero = int(voto)
            
            if numero == 0:
                messagebox.showinfo("Sucesso", "Voto registrado como BRANCO")
            elif numero in candidatos:
                candidatos[numero].votos += 1  
                salvar_candidatos(candidatos)  
                messagebox.showinfo("Sucesso", f"Voto registrado para o candidato: {candidatos[numero].__str__()}")
            else:
                messagebox.showinfo("Sucesso", "Voto registrado como NULO")
        else:
            messagebox.showwarning("Erro", "Digite um número válido.")
        
        entrada_voto.delete(0, tk.END)  
  
    urna_window = tk.Toplevel()
    urna_window.title("Urna Eletrônica")
    
    tk.Label(urna_window, text=f"Bem-vindo, {eleitor.__str__()}", justify="left").pack(pady=10)
    tk.Label(urna_window, text="Digite o número do candidato ou 0 para Branco:").pack(pady=5)
    entrada_voto = tk.Entry(urna_window)
    entrada_voto.pack(pady=5)
    
    tk.Button(urna_window, text="Votar", command=votar).pack(pady=10)

def salvar_candidatos(candidatos):
    with open("candidatos.pkl", "wb") as arquivo:
        pickle.dump(candidatos, arquivo)

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

tk.Label(root, text="Digite o título de eleitor:").pack(pady=10)
entrada_titulo = tk.Entry(root)
entrada_titulo.pack(pady=5)

tk.Button(root, text="Verificar", command=verificar_titulo).pack(pady=10)

root.mainloop()
