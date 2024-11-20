# Simulação de Urna Eletrônica em Python

Este projeto consiste no desenvolvimento de uma interface gráfica (GUI) simulando uma urna eletrônica, utilizando o módulo `tkinter` do Python. A aplicação permite realizar o processo de votação de forma interativa, simulando funcionalidades reais de uma urna.

## Funcionalidades

- **Carregamento de Dados:** 
  - A urna carrega a lista de candidatos e eleitores a partir de arquivos no formato `.pkl` ou `.csv`.
  
- **Validação de Eleitor:** 
  - Solicita o número do título do eleitor, verifica a existência no cadastro e apresenta os dados na tela.

- **Registro de Votos:**
  - Permite que o eleitor registre seu voto digitando o número do candidato.
  - Permite também votos em branco ou inválidos.

- **Armazenamento de Votos:**
  - Cada voto é computado e armazenado em um arquivo `.pkl` para futura apuração.

- **Fluxo Contínuo:**
  - Após o registro do voto, retorna para a tela inicial para o cadastro de um novo eleitor.

## Tecnologias Utilizadas

- **Linguagem:** Python 3.x
- **Bibliotecas:** 
  - `tkinter` (para a interface gráfica)
  - `pickle` (para manipulação de arquivos `.pkl`)
  - `csv` (para leitura e escrita de arquivos `.csv`)

## Estrutura do Projeto

.
├── data/                 
│   ├── eleitores.pkl      # Dados de eleitores cadastrados
│   ├── candidatos.pkl     # Dados de candidatos
│   ├── votos.pkl          # Registro de votos computados
├── main.py                # Arquivo principal da aplicação
├── utils/                 
│   ├── leitor_csv.py      # Funções para manipulação de arquivos CSV
│   ├── manipulador_dados.py # Funções para manipulação de dados em .pkl
└── README.md              # Documentação do projeto


## Como Executar

1. **Instale o Python 3.x**
   - Verifique se o Python está instalado: `python --version`
   - Caso não esteja, baixe-o [aqui](https://www.python.org/downloads/).

2. **Clone o Repositório**

   git clone https://github.com/usuario/simulacao-urna-eletronica.git
   cd simulacao-urna-eletronica

3. **Prepare os Arquivos de Dados**
   - Adicione os arquivos `.pkl` ou `.csv` contendo os eleitores e candidatos na pasta `data/`.

4. **Execute a Aplicação**
  
   python main.py

## Após a Execução

- **Tela Inicial:** Ao iniciar o programa, será solicitado o número do título do eleitor. O sistema irá validar o eleitor e mostrar os dados na tela.
- **Votação:** Após a validação, o eleitor pode votar digitando o número do candidato ou optar por votar em branco ou inválido.
- **Armazenamento:** O voto será computado e armazenado no arquivo `.pkl`. O programa então retornará à tela inicial para que outro eleitor possa registrar seu voto.
- **Repetição:** O sistema continuará esse ciclo até que a aplicação seja encerrada.

## Contribuidores

- Nicoly Lima - [nicoly.lima@unisantos.br](mailto:nicoly.lima@unisantos.br)
- Daniel Quintela - [danielquintelamuniz@unisantos.br](mailto:danielquintelamuniz@unisantos.br)
- Fernanda Meireles - [fernanda.meireles@unisantos.br](mailto:fernanda.meireles@unisantos.br)
- Rafaela Santana - [rafaela.santana@unisantos.br](mailto:rafaela.santana@unisantos.br)

## Observações

1. Certifique-se de que os arquivos `.pkl` ou `.csv` estejam no formato correto para evitar erros de leitura.
2. A aplicação é apenas uma simulação e não deve ser usada em contextos reais de votação.
3. Para dúvidas ou sugestões, entre em contato pelo e-mail [nicoly.lima@unisantos.br](mailto:nicoly.lima@unisantos.br).

