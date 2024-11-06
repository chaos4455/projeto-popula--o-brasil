# Criação de Dados Sintéticos 🤖

**Elias Andrade** - Arquiteto de Soluções Replika AI Solutions, Maringá - PR, 06/11/2024

**Versão:** 1.0

Este documento descreve o processo de geração de dados sintéticos para o projeto de previsão da população brasileira.  Dados sintéticos são usados para testar e validar o modelo de previsão antes de aplicar o modelo a dados reais.  A geração de dados sintéticos é uma técnica comum em aprendizado de máquina, especialmente quando os dados reais são limitados ou difíceis de obter.  Imagine isso como construir um protótipo antes de construir o produto final.

## Método de Geração

O script `criacao_dados.py` gera dados sintéticos utilizando interpolação cúbica e adição de ruído gaussiano.  A interpolação cúbica é usada para estimar a população em anos intermediários, baseando-se nos dados reais do IBGE.  O ruído gaussiano é adicionado para simular a variabilidade inerente aos dados reais.  A escolha da interpolação cúbica e da adição de ruído gaussiano foi feita considerando a natureza dos dados e o objetivo do projeto.  A interpolação cúbica é um método suave que preserva a tendência dos dados, enquanto o ruído gaussiano adiciona uma dose de realismo aos dados sintéticos.

O script utiliza os dados do IBGE como base para a interpolação.  Os dados do IBGE são considerados confiáveis e representativos da população brasileira.  A escolha dos dados do IBGE foi feita considerando a sua disponibilidade e confiabilidade.

## Dados do IBGE

Os dados do IBGE utilizados são:

| Ano | População (milhões) |
|---|---|
| 1950 | 51.9 |
| 1960 | 70.2 |
| 1970 | 93.1 |
| 1980 | 119.0 |
| 1990 | 146.6 |
| 2000 | 175.8 |
| 2010 | 195.7 |
| 2020 | 212.6 |
| 2025 | 216.4 |

## Saída

O script gera um arquivo Excel (`src/data/raw/datasetfake/populacao_brasil.xlsx`) contendo os dados sintéticos gerados.  Este arquivo é usado como entrada para o processo de normalização dos dados.  A escolha do formato Excel foi feita considerando a facilidade de leitura e manipulação dos dados.

## Bibliotecas Utilizadas

- `pandas`: Para manipulação de dados. 🐼
- `xlsxwriter`: Para gerar arquivos Excel. 📊
- `numpy`: Para operações numéricas. 🧮
- `scipy.interpolate`: Para interpolação. 📈

---

**[Elias Andrade](https://www.linkedin.com/in/eliasandrade)**
