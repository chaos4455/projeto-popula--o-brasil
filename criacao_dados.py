import pandas as pd
import xlsxwriter
import os
import numpy as np
from scipy.interpolate import interp1d

def gerar_dados_populacao(ano_inicio, ano_fim, dados_ibge):
    """Gera dados sintéticos de população do Brasil, baseados em dados do IBGE."""

    # Dados do IBGE fornecidos pelo usuário
    df_ibge = pd.DataFrame(dados_ibge)
    df_ibge['População'] = df_ibge['População'] * 1000000 # Convertendo para número inteiro

    # Interpolação para obter dados para todos os anos
    f = interp1d(df_ibge['Ano'], df_ibge['População'], kind='cubic') # Interpolação cúbica
    anos = np.arange(ano_inicio, ano_fim + 1)
    populacao_interpolada = f(anos)

    # Adicionando ruído para simular variações reais (ajuste do desvio padrão)
    desvio_padrao_ruido = np.std(df_ibge['População']) * 0.01 # 1% do desvio padrão dos dados do IBGE
    ruido = np.random.normal(0, desvio_padrao_ruido, len(populacao_interpolada))
    populacao = [int(p + r) for p, r in zip(populacao_interpolada, ruido)]

    df = pd.DataFrame({'Ano': anos, 'População': populacao})
    return df


def criar_dataset_populacao(df, xlsx_filepath):
    try:
        os.makedirs(os.path.dirname(xlsx_filepath), exist_ok=True) # Cria o diretório se não existir
        workbook = xlsxwriter.Workbook(xlsx_filepath)
        sheet = workbook.add_worksheet()
        sheet.freeze_panes(1, 1)

        sheet.write_row(0, 0, df.columns.tolist())  # Cabeçalho

        for i, row in df.iterrows():
            sheet.write_row(i + 1, 0, row.tolist())

        workbook.close()
        print(f"Arquivo '{xlsx_filepath}' criado com sucesso!")

    except Exception as e:
        print(f"Erro durante a criação do arquivo: {e}")


if __name__ == "__main__":
    ano_inicio = 1950
    ano_fim = 2025
    xlsx_filepath = 'datasetfake/populacao_brasil.xlsx'
    dados_ibge = [
        {'Ano': 1950, 'População': 51.9},
        {'Ano': 1960, 'População': 70.2},
        {'Ano': 1970, 'População': 93.1},
        {'Ano': 1980, 'População': 119.0},
        {'Ano': 1990, 'População': 146.6},
        {'Ano': 2000, 'População': 175.8},
        {'Ano': 2010, 'População': 195.7},
        {'Ano': 2020, 'População': 212.6},
        {'Ano': 2025, 'População': 216.4}
    ]
    df = gerar_dados_populacao(ano_inicio, ano_fim, dados_ibge)
    criar_dataset_populacao(df, xlsx_filepath)
