import pandas as pd
import xlsxwriter
import os
import numpy as np
from scipy.interpolate import interp1d

class IBGEData:
    def __init__(self, data):
        self.data = pd.DataFrame(data)
        self.data['População'] = self.data['População'] * 1000000

class PopulationDataGenerator:
    def generate_population_data(self, start_year, end_year, ibge_data):
        f = interp1d(ibge_data.data['Ano'], ibge_data.data['População'], kind='cubic')
        years = np.arange(start_year, end_year + 1)
        interpolated_population = f(years)

        std_noise = np.std(ibge_data.data['População']) * 0.01
        noise = np.random.normal(0, std_noise, len(interpolated_population))
        population = [int(p + r) for p, r in zip(interpolated_population, noise)]

        df = pd.DataFrame({'Ano': years, 'População': population})
        return df

class DatasetCreator:
    def create_dataset(self, df, filepath):
        try:
            os.makedirs(os.path.dirname(filepath), exist_ok=True)
            workbook = xlsxwriter.Workbook(filepath)
            sheet = workbook.add_worksheet()
            sheet.freeze_panes(1, 1)
            sheet.write_row(0, 0, df.columns.tolist())
            for i, row in df.iterrows():
                sheet.write_row(i + 1, 0, row.tolist())
            workbook.close()
            print(f"Arquivo '{filepath}' criado com sucesso!")
        except Exception as e:
            print(f"Erro durante a criação do arquivo: {e}")

if __name__ == "__main__":
    start_year = 1950
    end_year = 2025
    filepath = 'datasetfake/populacao_brasil.xlsx'
    ibge_data = [
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

    generator = PopulationDataGenerator()
    creator = DatasetCreator()
    ibge_data_obj = IBGEData(ibge_data)
    df = generator.generate_population_data(start_year, end_year, ibge_data_obj)
    creator.create_dataset(df, filepath)
