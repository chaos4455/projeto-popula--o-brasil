import subprocess
import time
from rich.console import Console
from rich.progress import track
from rich.panel import Panel
from rich.prompt import Confirm

console = Console()

def run_script(script_path):
    try:
        console.print(f"[bold blue]Executando:[/] {script_path}")
        result = subprocess.run(['python', script_path], capture_output=True, text=True, check=True)
        console.print(f"[bold green]Concluído:[/] {script_path}\n[italic]{result.stdout}[/]")
        return True
    except subprocess.CalledProcessError as e:
        console.print(f"[bold red]Erro ao executar:[/] {script_path}")
        console.print(f"[italic red]{e.stderr}[/]")
        return False
    except FileNotFoundError:
        console.print(f"[bold red]Erro:[/] Script '{script_path}' não encontrado.")
        return False
    except Exception as e:
        console.print(f"[bold red]Erro inesperado:[/] {e}")
        return False


def main():
    console.print(Panel.fit("[bold magenta]Iniciando Pipeline de Processamento de Dados[/]", title="Pipeline", style="bold magenta"))

    scripts = [
        'criacao_dados.py',
        'normalizacao_dados.py',
        'treinamento_modelo.py',
        'consumo_modelo.py'
    ]

    for script in track(scripts, description="Processando..."):
        if not run_script(script):
            if not Confirm.ask("Deseja continuar mesmo com erros?"):
                break

    console.print(Panel.fit("[bold green]Pipeline Concluído![/]", title="Pipeline", style="bold green"))


if __name__ == "__main__":
    main()
