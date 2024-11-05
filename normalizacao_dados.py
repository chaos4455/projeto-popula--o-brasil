import pandas as pd
import os
import logging
from sklearn.preprocessing import MinMaxScaler

# Configure logging
logging.basicConfig(filename='normalizacao_log.txt', level=logging.INFO, 
                    format='%(asctime)s - %(levelname)s - %(message)s')

def normalize_data():
    xlsx_filepath = 'datasetfake/populacao_brasil.xlsx'
    csv_filepath = 'datasetnormalizado/populacao_brasil.csv'

    if not os.path.exists('datasetnormalizado'):
        os.makedirs('datasetnormalizado')

    try:
        df = pd.read_excel(xlsx_filepath)
        
        # Check if the 'População' column exists
        if 'População' not in df.columns:
            logging.error(f"Erro: A coluna 'População' não foi encontrada no arquivo {xlsx_filepath}.")
            print(f"Erro: A coluna 'População' não foi encontrada no arquivo {xlsx_filepath}.")
            return

        # Normalizar a coluna 'População' usando MinMaxScaler
        scaler = MinMaxScaler()
        df['População'] = scaler.fit_transform(df[['População']])
        df.to_csv(csv_filepath, index=False)
        logging.info(f"Dados normalizados salvos em {csv_filepath}")
        print(f"Dados normalizados salvos em {csv_filepath}")
    except FileNotFoundError:
        logging.error(f"Erro: Arquivo {xlsx_filepath} não encontrado.")
        print(f"Erro: Arquivo {xlsx_filepath} não encontrado.")
    except Exception as e:
        logging.exception(f"Erro durante a normalização: {e}")
        print(f"Erro durante a normalização: {e}")


if __name__ == "__main__":
    normalize_data()
