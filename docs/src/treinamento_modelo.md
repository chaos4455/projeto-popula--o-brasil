# Treinamento do Modelo de Previsão 🧠

**Elias Andrade** - Arquiteto de Soluções Replika AI Solutions, Maringá - PR, 06/11/2024

**Versão:** 1.0

Este documento descreve o processo de treinamento do modelo de aprendizado de máquina utilizado para prever a população brasileira. O modelo escolhido é uma rede neural artificial (RNA) simples, devido à sua capacidade de modelar relações complexas entre as variáveis.  Imagine a RNA como um cérebro artificial, aprendendo padrões nos dados para fazer previsões precisas.

## Arquitetura do Modelo

O modelo utilizado é uma rede neural sequencial com duas camadas densas:

- Camada 1: 128 neurônios, função de ativação ReLU.
- Camada 2: 64 neurônios, função de ativação ReLU.
- Camada de Saída: 1 neurônio (para a previsão da população).

A função de ativação ReLU (Rectified Linear Unit) é escolhida por sua eficiência e simplicidade.  A escolha da arquitetura foi feita considerando o tamanho do conjunto de dados e a complexidade do problema.  Uma arquitetura mais complexa poderia levar a overfitting, enquanto uma arquitetura mais simples poderia não capturar a complexidade dos dados.  O equilíbrio entre complexidade e simplicidade é crucial para o desempenho do modelo.

## Processo de Treinamento

O script `treinamento_modelo.py` carrega os dados normalizados do arquivo `src/data/processed/datasetnormalizado/populacao_brasil.csv`, divide os dados em conjuntos de treinamento e teste (80% para treinamento e 20% para teste), e treina o modelo utilizando o otimizador Adam e a função de perda MSE (Mean Squared Error).  O treinamento é realizado por 100 épocas, com tamanho de lote de 32 amostras.  A escolha do otimizador Adam e da função de perda MSE foi feita considerando sua eficácia em problemas de regressão.

## Avaliação do Modelo

Após o treinamento, o modelo é avaliado utilizando o conjunto de teste.  A perda MSE é usada como métrica de avaliação.  A perda MSE representa a média dos erros quadrados entre as previsões do modelo e os valores reais.  Um valor menor de MSE indica um melhor desempenho do modelo.  O valor da perda MSE é registrado em um arquivo de log (`treinamento_log.txt`).

## Salvamento do Modelo

O modelo treinado é salvo no arquivo `src/models/models/modelo.h5` utilizando a biblioteca Keras.  Este arquivo pode ser carregado posteriormente para fazer previsões.  A escolha do formato HDF5 foi feita considerando sua compatibilidade com a biblioteca Keras.

## Bibliotecas Utilizadas

- `pandas`: Para manipulação de dados. 🐼
- `keras`: Para construção e treinamento do modelo. 🧠
- `scikit-learn`: Para divisão dos dados em conjuntos de treinamento e teste. 🤖
- `logging`: Para registro de logs. 📝

---

**[Elias Andrade](https://www.linkedin.com/in/eliasandrade)**
