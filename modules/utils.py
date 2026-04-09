import os

def clear_console():
    """
        Fonction qui permet de clear le terminal
        ATTENTION : Risque de ne pas fonctionner dans un terminal intégré type VS Code
    """
    print("\033[H\033[J", end="")