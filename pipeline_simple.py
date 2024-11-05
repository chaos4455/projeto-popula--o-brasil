import subprocess
import time

def run_script(script_path):
    try:
        print(f"Executando: {script_path}")
        subprocess.run(['python', script_path], check=True)
        print(f"Concluído: {script_path}")
        return True
    except subprocess.CalledProcessError as e:
        print(f"Erro ao executar: {script_path}")
        print(e)
        return False
    except FileNotFoundError:
        print(f"Erro: Script '{script_path}' não encontrado.")
        return False
    except Exception as e:
        print(f"Erro inesperado: {e}")
        return False


def main():
    scripts = [
        'criacao_dados.py',
        'normalizacao_dados.py',
        'treinamento_modelo.py',
        'consumo_modelo.py'
    ]

    for script in scripts:
        if not run_script(script):
            break

    print("Pipeline Concluído!")


if __name__ == "__main__":
    main()
