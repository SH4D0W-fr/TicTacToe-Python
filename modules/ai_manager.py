from groq import Groq
import modules.utils as utils

def get_key_from_env():
    """
    Récupère la clé API depuis les variables d'environnement
    """
    return utils.get_env("GROQ_API_KEY")


def save_key_to_env(api_key):
    """
    Enregistre la clé API dans les variables d'environnement
    """
    utils.set_env("GROQ_API_KEY", api_key)


def validate_api_key(api_key):
    """
    Valide la clé API en testant la connexion à Groq
    """
    try:
        test_client = Groq(api_key=api_key)
        test_client.models.list()
        return True
    except Exception:
        return False


def get_key():
    """
    Récupère et valide la clé API Groq
    """
    api_key = get_key_from_env()

    while True:
        if not api_key:
            print("\033[91m" + "Aucune clé API enregistrée" + "\033[0m")
            api_key = input("Clé API : ").strip()

        if validate_api_key(api_key):
            save_key_to_env(api_key)
            return api_key

        print("\033[91m" + "Clé API invalide" + "\033[0m")
        api_key = None


# Initialiser la clé et le client seulement quand nécessaire
_client = None

def get_client():
    """
    Obtient le client Groq, en initialisant la clé si nécessaire
    """
    global _client
    if _client is None:
        api_key = get_key()
        _client = Groq(api_key=api_key)
    return _client

def ai_play(tableau):
    prompt = f"""
        Tu joues au morpion (tic-tac-toe).

        Voici le plateau actuel :
        {tableau}

        Les cases sont nommées comme ceci :
        A1 A2 A3
        B1 B2 B3
        C1 C2 C3

        Règles :
        - Tu dois choisir la MEILLEURE case pour gagner ou empêcher l'adversaire de gagner.
        - Réponds uniquement avec UNE case valide (ex: A1, B3, C2).
        - Ne mets RIEN d'autre dans ta réponse.
    """

    client = get_client()
    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {"role": "user", "content": prompt}
        ],
        temperature=0
    )

    coup = response.choices[0].message.content
    if coup is None:
        coup = ""
    else:
        coup = coup.strip()

    return coup