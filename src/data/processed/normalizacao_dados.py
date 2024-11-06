import pandas as pd
import os
import logging
from sklearn.preprocessing import MinMaxScaler

# Configure logging
logging.basicConfig(filename='normalizacao_log.txt', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

class DataProcessor:
    def __init__(self, filepath):
        self.filepath = filepath
        self.df = None

    def load_data(self):
        try:
            if self.filepath.endswith('.xlsx'):
                self.df = pd.read_excel(self.filepath)
            elif self.filepath.endswith('.csv'):
                self.df = pd.read_csv(self.filepath)
            else:
                raise ValueError("Unsupported file format.")
            return True
        except FileNotFoundError:
            logging.error(f"Erro: Arquivo {self.filepath} não encontrado.")
            print(f"Erro: Arquivo {self.filepath} não encontrado.")
            return False
        except Exception as e:
            logging.exception(f"Erro durante a leitura do arquivo: {e}")
            print(f"Erro durante a leitura do arquivo: {e}")
            return False

    def save_data(self, filepath):
        try:
            os.makedirs(os.path.dirname(filepath), exist_ok=True)
            if filepath.endswith('.xlsx'):
                self.df.to_excel(filepath, index=False)
            elif filepath.endswith('.csv'):
                self.df.to_csv(filepath, index=False)
            else:
                raise ValueError("Unsupported file format.")
            logging.info(f"Dados salvos em {filepath}")
            print(f"Dados salvos em {filepath}")
            return True
        except Exception as e:
            logging.exception(f"Erro durante a gravação do arquivo: {e}")
            print(f"Erro durante a gravação do arquivo: {e}")
            return False


class Normalizer(DataProcessor):
    def normalize(self, column_name):
        if self.df is None or not self.load_data():
            return False

        if column_name not in self.df.columns:
            logging.error(f"Erro: A coluna '{column_name}' não foi encontrada.")
            print(f"Erro: A coluna '{column_name}' não foi encontrada.")
            return False

        scaler = MinMaxScaler()
        self.df[column_name] = scaler.fit_transform(self.df[[column_name]])
        return True


if __name__ == "__main__":
    xlsx_filepath = 'datasetfake/populacao_brasil.xlsx'
    csv_filepath = 'datasetnormalizado/populacao_brasil.csv'

    normalizer = Normalizer(xlsx_filepath)
    if normalizer.normalize('População'):
        normalizer.save_data(csv_filepath)
