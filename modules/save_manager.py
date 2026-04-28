import csv
from pathlib import Path

# Chemin du fichier CSV
DATA_FILE = Path(__file__).resolve().parent.parent / "data.csv"


def initialiser_csv():
    """
    Initialise le fichier CSV s'il n'existe pas
    """
    if not DATA_FILE.exists():
        with open(DATA_FILE, "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f, delimiter=";")
            writer.writerow(["pseudo", "victoires", "défaites", "nuls"])


def ajouter_ou_mettre_a_jour(pseudo: str, resultat: str):
    """
    Ajoute ou met à jour les stats d'un joueur
    resultat: "victoire", "défaite" ou "nul"
    """
    initialiser_csv()
    
    donnees = lire_tous_joueurs()
    
    # Chercher le joueur existant
    joueur_trouve = False
    for joueur in donnees:
        if joueur["pseudo"] == pseudo:
            joueur_trouve = True
            # Mettre à jour les stats - convertir le singulier en pluriel
            resultat_pluriel = resultat + "s" if resultat != "nul" else "nuls"
            joueur[resultat_pluriel] = str(int(joueur.get(resultat_pluriel, 0)) + 1)
            break
    
    # Si pas trouvé, créer un nouveau joueur
    if not joueur_trouve:
        nouveau_joueur = {"pseudo": pseudo, "victoires": "0", "défaites": "0", "nuls": "0"}
        # Incrémenter la stat correspondante
        resultat_pluriel = resultat + "s" if resultat != "nul" else "nuls"
        nouveau_joueur[resultat_pluriel] = "1"
        donnees.append(nouveau_joueur)
    
    # Réécrire le fichier
    ecrire_donnees(donnees)


def lire_tous_joueurs() -> list[dict]:
    """
    Retourne la liste de tous les joueurs avec leurs stats
    """
    initialiser_csv()
    donnees = []
    
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f, delimiter=";")
        for row in reader:
            if row and row.get("pseudo"):  # Vérifier que la ligne n'est pas vide
                donnees.append(row)
    
    return donnees


def obtenir_stats_joueur(pseudo: str) -> dict | None:
    """
    Retourne les stats d'un joueur spécifique
    """
    joueurs = lire_tous_joueurs()
    for joueur in joueurs:
        if joueur["pseudo"] == pseudo:
            return joueur
    return None


def ecrire_donnees(donnees: list[dict]):
    """
    Écrit les données dans le fichier CSV
    """
    # Déterminer toutes les colonnes possibles
    colonnes = ["pseudo"]
    colonnes_stats = set()
    for joueur in donnees:
        for cle in joueur.keys():
            if cle != "pseudo":
                colonnes_stats.add(cle)
    
    colonnes.extend(sorted(colonnes_stats))
    
    with open(DATA_FILE, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=colonnes, delimiter=";")
        writer.writeheader()
        writer.writerows(donnees)

def trier_classement(joueurs: list[dict]) -> list[dict]:
    """
    Trie les joueurs par victoires, puis nuls, puis défaites.
    """
    # Bubble sort inversé avec un classement multi-critères
    n = len(joueurs)
    for i in range(n):
        for j in range(0, n - i - 1):
            # On construit un score comparable pour chaque joueur.
            # Plus il y a de victoires, mieux c'est.
            # En cas d'égalité, on départage avec les nuls, puis on pénalise les défaites.
            score_gauche = (
                int(joueurs[j].get("victoires", 0)),
                int(joueurs[j].get("nuls", 0)),
                -int(joueurs[j].get("défaites", 0)),
            )
            score_droite = (
                int(joueurs[j + 1].get("victoires", 0)),
                int(joueurs[j + 1].get("nuls", 0)),
                -int(joueurs[j + 1].get("défaites", 0)),
            )

            # Si le joueur de gauche est moins bien classé, on échange les deux entrées.
            if score_gauche < score_droite:
                # Échanger les éléments
                joueurs[j], joueurs[j + 1] = joueurs[j + 1], joueurs[j]
    
    return joueurs


def obtenir_classement() -> list[dict]:
    """
    Retourne la liste des joueurs triés selon la hiérarchie victoires, nuls, défaites.
    """
    joueurs = lire_tous_joueurs()
    
    joueurs_tries = trier_classement(joueurs)
    
    return joueurs_tries
