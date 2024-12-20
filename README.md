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

## Contribuidores

- Fernanda Meireles - [fernanda.meireles@unisantos.br](mailto:fernanda.meireles@unisantos.br)
- Nicoly Lima - [nicoly.lima@unisantos.br](mailto:nicoly.lima@unisantos.br)
- Rafaela Santana - [rafaela.santana@unisantos.br](mailto:rafaela.santana@unisantos.br)

## Observações

1. Certifique-se de que os arquivos `.pkl` ou `.csv` estejam no formato correto para evitar erros de leitura.
2. A aplicação é apenas uma simulação e não deve ser usada em contextos reais de votação.
3. Para dúvidas ou sugestões, entre em contato pelo e-mail [nicoly.lima@unisantos.br](mailto:nicoly.lima@unisantos.br).

