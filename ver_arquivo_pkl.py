import pickle

def abrir_arquivo_pkl(nome_arquivo):
    try:
        with open(nome_arquivo, 'rb') as arquivo:
            dados = pickle.load(arquivo)
            print(dados)
    except FileNotFoundError:
        print(f"Arquivo {nome_arquivo} não encontrado.")
    except Exception as e:
        print(f"Erro ao abrir o arquivo: {e}")

# Substitua pelo caminho do arquivo .pkl que você deseja inspecionar
#abrir_arquivo_pkl('eleitores.pkl')
abrir_arquivo_pkl('candidatos.pkl')
