plateau = [[".", ".", "."], [".", ".", "."], [".", ".", "."]]

def affiche():
    """
    Retourne le plateau avec coordonnées (A B C en haut, 1 2 3 à gauche)
    Code fourni modifié pour l'adapter à notre disposition
    """
    
    # En tête du plateau
    output = "\t \t  A B C\n"
    
    # Plateau avec coordonnées
    for j in range(len(plateau)):
        output += f"\t \t {j + 1} "
        for i in range(len(plateau[j])):
            output += plateau[j][i] + " "
        output += "\n"
    
    return output, plateau

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

def point_setter(pos:str, symbol:str) -> bool:
    """
        Fonction qui permet de placer un point sur la position souhaitée
    """
    if point_checker(pos):
        if plateau[int(pos[1]) - 1][ord(pos[0]) - ord("A")] == ".":
            plateau[int(pos[1]) - 1][ord(pos[0]) - ord("A")] = symbol
            return True
    return False