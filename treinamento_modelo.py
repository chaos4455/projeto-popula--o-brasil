# Importações necessárias
import pandas as pd
import numpy as np
from keras.models import Sequential
from keras.layers import Dense
from sklearn.model_selection import train_test_split
import os

# Carrega os dados
try:
    df = pd.read_csv('datasetnormalizado/populacao_brasil.csv')
    X = df['Ano'].values.reshape(-1, 1)
    y = df['População'].values

    #Verifica se os dados foram carregados corretamente
    if len(X) == 0 or len(y) == 0:
        raise ValueError("Dados não carregados corretamente.")

    # Divide os dados em conjuntos de treinamento e teste
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Cria o modelo
    modelo = Sequential()
    modelo.add(Dense(128, activation='relu', input_shape=(1,)))
    modelo.add(Dense(64, activation='relu'))
    modelo.add(Dense(1))

    # Compila o modelo
    modelo.compile(optimizer='adam', loss='mse')

    # Treina o modelo
    modelo.fit(X_train, y_train, epochs=100, batch_size=32, verbose=1)

    # Avalia o modelo
    loss = modelo.evaluate(X_test, y_test, verbose=0)
    print(f'Loss do modelo: {loss}')

    # Salva o modelo
    os.makedirs('models', exist_ok=True)
    modelo.save('models/modelo.h5')
    print('Modelo salvo em models/modelo.h5')

except FileNotFoundError:
    print("Erro: Arquivo 'datasetnormalizado/populacao_brasil.csv' não encontrado.")
except pd.errors.EmptyDataError:
    print("Erro: O arquivo CSV está vazio.")
except KeyError as e:
    print(f"Erro: Coluna '{e.args[0]}' não encontrada no arquivo CSV.")
except ValueError as e:
    print(f"Erro: {e}")
except Exception as e:
    print(f"Erro inesperado durante o treinamento: {e}")
