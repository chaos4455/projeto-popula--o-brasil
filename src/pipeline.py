import subprocess
import time
from rich.console import Console
from rich.progress import track
from rich.panel import Panel
from rich.prompt import Confirm

console = Console()

class ScriptExecutor:
    def execute(self, script_path):
        try:
            console.print(f"[bold blue]Executando:[/] {script_path}")
            result = subprocess.run(['python', script_path], capture_output=True, text=True, check=True)
            console.print(f"[bold green]Concluído:[/] {script_path}\n[italic]{result.stdout}[/]")
            return True, ""
        except subprocess.CalledProcessError as e:
            console.print(f"[bold red]Erro ao executar:[/] {script_path}")
            console.print(f"[italic red]{e.stderr}[/]")
            return False, e.stderr
        except FileNotFoundError:
            console.print(f"[bold red]Erro:[/] Script '{script_path}' não encontrado.")
            return False, f"Script '{script_path}' não encontrado."
        except Exception as e:
            console.print(f"[bold red]Erro inesperado:[/] {e}")
            return False, str(e)


class Pipeline:
    def __init__(self, scripts):
        self.scripts = scripts
        self.executor = ScriptExecutor()

    def run(self):
        console.print(Panel.fit("[bold magenta]Iniciando Pipeline de Processamento de Dados[/]", title="Pipeline", style="bold magenta"))

        for script in track(self.scripts, description="Processando..."):
            success, error_message = self.executor.execute(script)
            if not success:
                if not Confirm.ask(f"Erro em {script}: {error_message}\nDeseja continuar mesmo com erros?"):
                    break

        console.print(Panel.fit("[bold green]Pipeline Concluído![/]", title="Pipeline", style="bold green"))


if __name__ == "__main__":
    scripts = [
        'criacao_dados.py',
        'normalizacao_dados.py',
        'treinamento_modelo.py',
        'consumo_modelo.py'
    ]
    pipeline = Pipeline(scripts)
    pipeline.run()
