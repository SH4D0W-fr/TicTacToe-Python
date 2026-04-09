import os
import dotenv
from pathlib import Path

ENV_FILE = Path(__file__).resolve().parent.parent / ".env"

def clear_console():
    """
        Fonction qui permet de clear le terminal
        ATTENTION : Risque de ne pas fonctionner dans un terminal intégré type VS Code
    """
    print("\033[H\033[J", end="")

def set_env(name:str, value:str):
    """
        Fonction qui permet de créer des variables d'environnement
    """
    # Rend la variable disponible immédiatement dans le processus courant.
    os.environ[name] = value
    # Persiste aussi la variable dans .env pour les prochains lancements.
    if not ENV_FILE.exists():
        ENV_FILE.touch()
    dotenv.set_key(str(ENV_FILE), name, value)

def get_env(name:str) -> str | None:
    """
        Fonction qui permet de récupérer des variables d'environnement
    """
    dotenv.load_dotenv(dotenv_path=ENV_FILE)
    return os.getenv(name)