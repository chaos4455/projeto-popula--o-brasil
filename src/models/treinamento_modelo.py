import pandas as pd
import numpy as np
from keras.models import Sequential
from keras.layers import Dense
from sklearn.model_selection import train_test_split
import os
import logging

# Configure logging
logging.basicConfig(filename='treinamento_log.txt', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')


class DataHandler:
    def load_data(self, filepath):
        try:
            df = pd.read_csv(filepath)
            X = df['Ano'].values.reshape(-1, 1)
            y = df['População'].values
            if len(X) == 0 or len(y) == 0:
                raise ValueError("Dados não carregados corretamente.")
            return X, y
        except FileNotFoundError:
            logging.error(f"Erro: Arquivo {filepath} não encontrado.")
            raise
        except KeyError as e:
            logging.error(f"Erro: Coluna '{e.args[0]}' não encontrada.")
            raise
        except Exception as e:
            logging.exception(f"Erro durante a leitura dos dados: {e}")
            raise


class ModelTrainer:
    def __init__(self, model_architecture):
        self.model_architecture = model_architecture

    def create_model(self, input_shape):
        model = Sequential()
        for layer in self.model_architecture:
            model.add(layer(input_shape=input_shape))
        return model

    def train_model(self, X_train, y_train, X_test, y_test):
        model = self.create_model(input_shape=(X_train.shape[1],))
        model.compile(optimizer='adam', loss='mse')
        model.fit(X_train, y_train, epochs=100, batch_size=32, verbose=1)
        loss = model.evaluate(X_test, y_test, verbose=0)
        logging.info(f'Loss do modelo: {loss}')
        return model, loss


class ModelSaver:
    def save_model(self, model, filepath):
        try:
            os.makedirs(os.path.dirname(filepath), exist_ok=True)
            model.save(filepath)
            logging.info(f'Modelo salvo em {filepath}')
            print(f'Modelo salvo em {filepath}')
        except Exception as e:
            logging.exception(f"Erro ao salvar o modelo: {e}")
            raise


if __name__ == "__main__":
    filepath = 'datasetnormalizado/populacao_brasil.csv'
    model_filepath = 'models/modelo.h5'
    model_architecture = [lambda input_shape: Dense(128, activation='relu', input_shape=input_shape),
                          lambda input_shape: Dense(64, activation='relu'),
                          lambda input_shape: Dense(1)]

    try:
        data_handler = DataHandler()
        X, y = data_handler.load_data(filepath)
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

        model_trainer = ModelTrainer(model_architecture)
        model, loss = model_trainer.train_model(X_train, y_train, X_test, y_test)

        model_saver = ModelSaver()
        model_saver.save_model(model, model_filepath)

    except Exception as e:
        print(f"Erro inesperado durante o treinamento: {e}")
