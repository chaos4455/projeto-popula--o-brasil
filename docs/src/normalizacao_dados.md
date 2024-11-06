# Normalização de Dados 📊

**Elias Andrade** - Arquiteto de Soluções Replika AI Solutions, Maringá - PR, 06/11/2024

**Versão:** 1.0

Este documento descreve o processo de normalização dos dados utilizados no projeto de previsão da população brasileira. A normalização é uma etapa crucial no pré-processamento de dados para aprendizado de máquina, pois garante que todas as features tenham a mesma escala, evitando que features com valores maiores dominem o processo de treinamento do modelo.  Imagine isso como nivelar o campo de jogo para todos os jogadores, garantindo uma competição justa.

## Processo de Normalização

O script `normalizacao_dados.py` utiliza a biblioteca `scikit-learn` para normalizar os dados. Especificamente, o `MinMaxScaler` é usado para transformar os valores da coluna 'População' para um intervalo entre 0 e 1.  Este método é escolhido por sua simplicidade e eficácia em muitos cenários.  A escolha do método de normalização é crucial, pois diferentes métodos têm diferentes propriedades e podem afetar o desempenho do modelo.  A escolha do MinMaxScaler foi feita considerando a natureza dos dados e o objetivo do projeto.

O script lê os dados de um arquivo Excel (`src/data/raw/datasetfake/populacao_brasil.xlsx`) e salva os dados normalizados em um arquivo CSV (`src/data/processed/datasetnormalizado/populacao_brasil.csv`).  O uso de arquivos CSV é preferível para o processamento de dados em aprendizado de máquina devido à sua simplicidade e eficiência.  A escolha do formato CSV foi feita considerando a compatibilidade com as bibliotecas de aprendizado de máquina utilizadas no projeto.

## Logs

O script gera um log detalhado em `normalizacao_log.txt`, registrando todas as etapas do processo, incluindo erros e avisos.  Este log é essencial para monitorar o processo de normalização e identificar possíveis problemas.  O log é um recurso valioso para a depuração e manutenção do sistema.  Imagine-o como um diário de bordo, registrando cada detalhe da jornada.

## Bibliotecas Utilizadas

- `pandas`: Para manipulação de dados. 🐼
- `scikit-learn`: Para normalização de dados. 🤖
- `logging`: Para registro de logs. 📝

---

**[Elias Andrade](https://www.linkedin.com/in/eliasandrade)**
