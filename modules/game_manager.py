def affiche():
    """
    Affiche le plateau avec coordonnées (A B C en haut, 1 2 3 à gauche)
    Code fourni modifié pour l'adapter à notre disposition
    """
    plateau = [[".", ".", "."], [".", ".", "."], [".", ".", "."]]

    # En-tête colonnes
    print("\t \t  A B C")

    # Affichage du plateau
    for j in range(len(plateau)):
        print("\t \t", j + 1, end=" ")
        for i in range(len(plateau[j])):
            print(plateau[j][i], end=" ")
        print()

def game_type_choice():
    """
        Fonction qui permet de choisir le mode de jeu (IA ou Algorithmique)
    """
    print("Souhaitez vous jouer contre un algorithme ou une IA (clé API Groq requise ❗)")
    choix = input("Votre choix (algo / ia) : ")
    if choix.lower() == "algo":
        a = 0
        # Appel de la fonction pour lancer le jeu en mode algo
    elif choix.lower() == 'ia':
        a = 0
        # Appel de la fonction pour lancer le jeu en mode IA
    else:
        print("Choix invalide. Veuillez réessayer")
        game_type_choice()

def point_checker(pos:str) -> bool:
    """
        Fonction qui permet de vérifier si un point spécifié est valide
    """
    valid = [f"{lettre}{chiffre}" for lettre in "ABC" for chiffre in range(1, 4)] # Liste par compréhension
    for v in valid:
        if pos == v:
             return True
    return False