# Previsão da População Brasileira 🎉

Olá! Sou Elias Andrade e neste projeto, utilizei uma rede neural para prever a população do Brasil nos próximos anos.  🚀

[![Python Version](https://img.shields.io/badge/python-3.x-blue.svg)](https://www.python.org/)
[![Pandas Version](https://img.shields.io/badge/pandas-latest-brightgreen.svg)](https://pandas.pydata.org/)
[![Scikit-learn Version](https://img.shields.io/badge/scikit--learn-latest-orange.svg)](https://scikit-learn.org/stable/)
[![TensorFlow Version](https://img.shields.io/badge/tensorflow-latest-yellow.svg)](https://www.tensorflow.org/)
[![Keras Version](https://img.shields.io/badge/keras-latest-purple.svg)](https://keras.io/)


## Descrição

Este projeto consiste em um pipeline que processa dados, treina um modelo de aprendizado de máquina e gera previsões.  As etapas são:

1. **Criação de Dados:** 📊 Criei um dataset sintético de população baseado em dados históricos do IBGE (disponíveis em [link para dados IBGE, se disponível]), utilizando interpolação cúbica e adição de ruído gaussiano para simular variações reais. O nível de ruído foi ajustado cuidadosamente para 5% do desvio padrão dos dados do IBGE, buscando um equilíbrio entre realismo e estabilidade do modelo.  Optei pela interpolação cúbica por sua capacidade de capturar tendências não-lineares nos dados. O dataset foi salvo em um arquivo Excel (`datasetfake/populacao_brasil.xlsx`).  (Arquivo: `criacao_dados.py`)

2. **Normalização de Dados:** 🔄 Normalizei os dados de população usando `MinMaxScaler` do scikit-learn.  Este método escala os dados para um intervalo entre 0 e 1, o que é benéfico para o treinamento de redes neurais, evitando que características com valores maiores dominem o processo de aprendizado. Os dados normalizados foram salvos em um arquivo CSV (`datasetnormalizado/populacao_brasil.csv`). (Arquivo: `normalizacao_dados.py`)

3. **Treinamento do Modelo:** 🧠 Treinei uma rede neural artificial (RNA) usando Keras para prever a população com base nos dados normalizados.  A arquitetura da RNA e a lógica de treinamento são detalhadas na seção abaixo. O modelo treinado foi salvo em um arquivo HDF5 (`models/modelo.h5`). (Arquivo: `treinamento_modelo.py`)

4. **Consumo do Modelo:** 📈 Carreguei o modelo treinado e gerei previsões para os próximos 50 anos (2025-2074). Os resultados foram salvos em diferentes formatos (CSV, JSON, YAML e TXT) na pasta `resultados`.  Um gráfico da previsão também foi gerado e salvo como `previsao_populacao.png`. (Arquivo: `consumo_modelo.py`)

## Tecnologias Utilizadas

* Python 🐍
* Pandas 🐼
* Scikit-learn 🤖
* Keras 🧠
* Matplotlib 📊
* Xlsxwriter xlsx
* Rich ✨
* YAML 📜
* NumPy 🔢
* SciPy 🧮


## Como Executar

1. Certifique-se de ter o Python 3 instalado, juntamente com as bibliotecas necessárias (Pandas, Scikit-learn, TensorFlow, Keras, Matplotlib, Xlsxwriter, Rich, PyYAML, NumPy, SciPy).  Você pode instalá-las usando `pip install pandas scikit-learn tensorflow matplotlib xlsxwriter rich pyyaml numpy scipy`.

2. Execute o script `pipeline.py` (recomendado) ou `pipeline_simple.py` (para uma versão mais simples sem a biblioteca rich).

## Resultados

Os resultados das previsões estão salvos na pasta `resultados` em diferentes formatos.  Um gráfico da previsão também foi gerado e salvo como `previsao_populacao.png`.  A precisão do modelo pode ser avaliada pela perda (MSE) obtida durante o treinamento e teste.  É importante notar que este é um modelo de previsão e sua precisão depende da qualidade dos dados e da complexidade do fenômeno em questão.

## Arquitetura e Lógica da Rede Neural ⚙️

A rede neural utilizada neste projeto é uma rede feedforward totalmente conectada (dense) com três camadas.  Escolhi essa arquitetura por sua simplicidade e eficácia para problemas de regressão, como a previsão da população.  Cada camada é descrita abaixo:

**Camada de Entrada:**
* Neurônios: 128
* Função de Ativação: ReLU (Rectified Linear Unit)  ➡️  `max(0, x)`
* Entrada: Um único valor representando o ano.

**Camada Oculta:**
* Neurônios: 64
* Função de Ativação: ReLU  ➡️  `max(0, x)`
* Esta camada extrai características mais complexas dos dados, aprendendo padrões não-lineares na relação entre o ano e a população.

**Camada de Saída:**
* Neurônios: 1
* Função de Ativação: Linear (nenhuma função de ativação) ➡️ `x`
* Saída: Um único valor representando a previsão da população.

**Otimizador:** Adam 
* Otimizador Adam foi escolhido por sua eficiência e adaptabilidade.

**Função de Perda:** MSE (Mean Squared Error)
* A função de perda MSE mede a diferença quadrática média entre as previsões do modelo e os valores reais da população.

**Treinamento:**
* Épocas: 100
* Tamanho do Lote (Batch Size): 32
* Utilizei um tamanho de lote maior para acelerar o treinamento, enquanto um número maior de épocas pode levar a um melhor ajuste dos dados, mas também pode aumentar o risco de overfitting.


## Considerações Futuras

* Incluir mais dados históricos do IBGE para melhorar a precisão do modelo.  Dados demográficos mais detalhados, como taxas de natalidade, mortalidade e migração, poderiam melhorar significativamente a precisão das previsões.
* Explorar outros modelos de aprendizado de máquina, como modelos ARIMA ou Prophet, para comparar a performance com a rede neural.
* Implementar uma interface gráfica para facilitar a visualização dos resultados e a interação com o modelo.
* Adicionar validação cruzada (cross-validation) para avaliar melhor a performance do modelo e reduzir o risco de overfitting.
* Implementar técnicas de regularização (como dropout ou L1/L2) para melhorar a generalização do modelo.
* Analisar a sensibilidade do modelo a diferentes parâmetros, como o nível de ruído adicionado aos dados sintéticos e a arquitetura da rede neural.


---

Feito por Elias Andrade, um engenheiro de software altamente qualificado.
