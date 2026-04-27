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
            writer.writerow(["pseudo", "victoires_algo", "défaites_algo", "nuls_algo", "victoires_ia", "défaites_ia", "nuls_ia"])


def ajouter_ou_mettre_a_jour(pseudo: str, resultat: str, mode: str):
    """
    Ajoute ou met à jour les stats d'un joueur
    resultat: "victoire", "défaite" ou "nul"
    mode: "algo" ou "ia"
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
            cle = f"{resultat_pluriel}_{mode}"
            joueur[cle] = str(int(joueur.get(cle, 0)) + 1)
            break
    
    # Si pas trouvé, créer un nouveau joueur
    if not joueur_trouve:
        nouveau_joueur = {"pseudo": pseudo}
        # Initialiser toutes les colonnes
        for resultat_type in ["victoire", "défaite", "nul"]:
            for mode_type in ["algo", "ia"]:
                # Convertir le singulier en pluriel pour la clé
                resultat_pluriel = resultat_type + "s" if resultat_type != "nul" else "nuls"
                cle = f"{resultat_pluriel}_{mode_type}"
                nouveau_joueur[cle] = "1" if resultat_type == resultat and mode_type == mode else "0"
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


def obtenir_stats_joueur(pseudo: str) -> dict:
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

def trier_classement(joueurs: list[dict], mode: str = None) -> list[dict]:
    """
    Trie les joueurs par nombre total de victoires en utilisant un bubble sort inversé
    mode: "algo", "ia" ou None (tous les modes)
    """
    # Calculer le total des victoires pour chaque joueur
    for joueur in joueurs:
        if mode == "algo":
            victoires = int(joueur.get("victoires_algo", 0))
        elif mode == "ia":
            victoires = int(joueur.get("victoires_ia", 0))
        else:
            victoires = int(joueur.get("victoires_algo", 0)) + int(joueur.get("victoires_ia", 0))
        
        joueur["total_victoires"] = victoires
    
    # Bubble sort inversé (ordre descendant)
    n = len(joueurs)
    for i in range(n):
        for j in range(0, n - i - 1):
            if joueurs[j]["total_victoires"] < joueurs[j + 1]["total_victoires"]:
                # Échanger les éléments
                joueurs[j], joueurs[j + 1] = joueurs[j + 1], joueurs[j]
    
    return joueurs


def obtenir_classement(mode: str = None) -> list[dict]:
    """
    Retourne les joueurs triés par nombre total de victoires en utilisant un bubble sort inversé
    mode: "algo", "ia" ou None (tous les modes)
    """
    joueurs = lire_tous_joueurs()
    
    joueurs_tries = trier_classement(joueurs, mode)
    
    return joueurs_tries
