import pandas as pd
import numpy as np
from keras.models import load_model
import matplotlib.pyplot as plt
import json
import yaml
import os

# Carrega o modelo treinado (sem recompilar)
try:
    modelo = load_model('models/modelo.h5', compile=False)
except FileNotFoundError:
    print("Erro: Modelo não encontrado em 'models/modelo.h5'. Certifique-se de que o treinamento foi concluído com sucesso.")
    exit(1)
except Exception as e:
    print(f"Erro ao carregar o modelo: {e}")
    exit(1)


# Dados para previsão (anos de 2025 a 2074)
anos_futuro = np.arange(2025, 2075).reshape(-1, 1)

# Faz previsões
try:
    previsoes = modelo.predict(anos_futuro)
except Exception as e:
    print(f"Erro durante a previsão: {e}")
    exit(1)


# Cria um DataFrame com os resultados
df_previsoes = pd.DataFrame({'ano': np.arange(2025, 2075), 'população': previsoes.flatten()})

# Converte a população para milhões
df_previsoes['população'] = df_previsoes['população'] / 1000000


# Gera gráficos
plt.figure(figsize=(10, 6))
plt.plot(df_previsoes['ano'], df_previsoes['população'])
plt.xlabel('Ano')
plt.ylabel('População (milhões)')
plt.title('Previsão da População para os Próximos 50 Anos')
plt.savefig('previsao_populacao.png')
plt.close()

# Salva os dados em diferentes formatos
os.makedirs('resultados', exist_ok=True)
try:
    df_previsoes.to_csv('resultados/previsao_populacao.csv', index=False, encoding='utf-8')
    df_previsoes.to_json('resultados/previsao_populacao.json', orient='records') #encoding removed
    with open('resultados/previsao_populacao.yaml', 'w', encoding='utf-8') as f:
        yaml.dump(df_previsoes.to_dict(orient='records'), f)
    with open('resultados/previsao_populacao.txt', 'w', encoding='utf-8') as f:
        f.write(df_previsoes.to_string(index=False))
except Exception as e:
    print(f"Erro ao salvar os resultados: {e}")
    exit(1)

print("Previsões geradas e salvas com sucesso!")
