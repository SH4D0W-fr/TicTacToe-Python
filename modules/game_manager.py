import modules.utils as utils
import modules.ai_manager as ai_manager

# Init variables globales
IA = "O"
HUMAIN = "X"
VIDE = "."

plateau = [[VIDE, VIDE, VIDE], [VIDE, VIDE, VIDE], [VIDE, VIDE, VIDE]]


def reinitialiser_plateau():
    """
    Fonction qui remet le plateau à zéro
    """
    global plateau
    plateau = [[VIDE, VIDE, VIDE], [VIDE, VIDE, VIDE], [VIDE, VIDE, VIDE]]

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


def plateau_en_liste(tableau: list) -> list[str]:
    """
    Fonction qui transforme le plateau 3x3 en liste d'une seule ligne
    """
    return [case for ligne in tableau for case in ligne]


def cases_libres(plateau_ligne: list[str]) -> list[int]:
    """
    Fonction qui récupère les indices des cases libres
    """
    return [i for i, case in enumerate(plateau_ligne) if case == VIDE]


def verifier_gagnant(plateau_ligne: list[str], symbole: str) -> bool:
    """
    Fonction qui vérifie si un symbole a gagné sur un plateau en ligne
    """
    combinaisons = [
        [0, 1, 2],
        [3, 4, 5],
        [6, 7, 8],
        [0, 3, 6],
        [1, 4, 7],
        [2, 5, 8],
        [0, 4, 8],
        [2, 4, 6],
    ]

    for a, b, c in combinaisons:
        if plateau_ligne[a] == plateau_ligne[b] == plateau_ligne[c] == symbole:
            return True

    return False


def indice_vers_pos(indice: int) -> str:
    """
    Fonction qui convertit un indice du minimax en position du plateau
    """
    ligne = indice // 3
    colonne = indice % 3
    return f"{chr(ord('A') + colonne)}{ligne + 1}"


def minimax(plateau_ligne: list[str], est_maximiseur: bool) -> int:
    """
    Fonction qui calcule le meilleur score possible pour l'algorithme
    """
    if verifier_gagnant(plateau_ligne, IA):
        return 1
    if verifier_gagnant(plateau_ligne, HUMAIN):
        return -1
    if not cases_libres(plateau_ligne):
        return 0

    if est_maximiseur:
        meilleur = -2
        for i in cases_libres(plateau_ligne):
            plateau_ligne[i] = IA
            score = minimax(plateau_ligne, False)
            plateau_ligne[i] = VIDE
            meilleur = max(meilleur, score)
        return meilleur
    else:
        meilleur = 2
        for i in cases_libres(plateau_ligne):
            plateau_ligne[i] = HUMAIN
            score = minimax(plateau_ligne, True)
            plateau_ligne[i] = VIDE
            meilleur = min(meilleur, score)
        return meilleur


def meilleur_coup(plateau_ligne: list[str]) -> int:
    """
    Fonction qui récupère le coup optimal pour l'algorithme
    """
    meilleur_score = -2
    coup_optimal = -1

    for i in cases_libres(plateau_ligne):
        plateau_ligne[i] = IA
        score = minimax(plateau_ligne, False)
        plateau_ligne[i] = VIDE

        if score > meilleur_score:
            meilleur_score = score
            coup_optimal = i

    return coup_optimal


def jouer_mode_algo(pseudo_joueur):
    """
    Fonction qui lance une partie contre l'algorithme
    Retourne un tuple (resultat, mode, pseudo_joueur) où resultat est 'victoire', 'défaite' ou 'nul'
    """
    reinitialiser_plateau()
    tour_humain = True

    while True:
        utils.clear_console()
        print(affiche()[0])

        etat_actuel = plateau_en_liste(plateau)

        if verifier_gagnant(etat_actuel, HUMAIN):
            print("Vous avez gagné !")
            return ("victoire", pseudo_joueur, "Algorithme")

        if verifier_gagnant(etat_actuel, IA):
            print("L'algorithme a gagné !")
            return ("défaite", "Algorithme", pseudo_joueur)

        if not cases_libres(etat_actuel):
            print("Match nul !")
            return ("nul", pseudo_joueur, "Algorithme")

        if tour_humain:
            coup = input("Votre coup : ").strip().upper()
            if point_setter(coup, HUMAIN):
                tour_humain = False
            else:
                print("Coup invalide. Réessayez.")
        else:
            coup_ia = meilleur_coup(etat_actuel)
            if coup_ia == -1:
                print("Match nul !")
                return ("nul", "algo", pseudo_joueur)

            point_setter(indice_vers_pos(coup_ia), IA)
            print(f"L'algorithme joue {indice_vers_pos(coup_ia)}")
            tour_humain = True

def jouer_mode_ia(pseudo_joueur):
    """
    Fonction qui lance une partie contre l'IA
    Retourne un tuple (resultat, mode, pseudo_joueur) où resultat est 'victoire', 'défaite' ou 'nul'
    """
    reinitialiser_plateau()
    tour_humain = True

    while True:
        utils.clear_console()
        print(affiche()[0])

        etat_actuel = plateau_en_liste(plateau)

        if verifier_gagnant(etat_actuel, HUMAIN):
            print("Vous avez gagné !")
            return ("victoire", pseudo_joueur, "IA")

        if verifier_gagnant(etat_actuel, IA):
            print("L'IA a gagné !")
            return ("défaite", "IA", pseudo_joueur)

        if not cases_libres(etat_actuel):
            print("Match nul !")
            return ("nul", pseudo_joueur, "IA")

        if tour_humain:
            coup = input("Votre coup : ").strip().upper()
            if point_setter(coup, HUMAIN):
                tour_humain = False
            else:
                print("Coup invalide. Réessayez.")
        else:
            coup_ia = ai_manager.ai_play(etat_actuel)
            if coup_ia == -1:
                print("Match nul !")
                return ("nul", pseudo_joueur, "IA")

            coup_ia = str(coup_ia).strip().upper()
            if not point_setter(coup_ia, IA):
                coup_ia = indice_vers_pos(meilleur_coup(etat_actuel))
                point_setter(coup_ia, IA)

            print(f"L'IA joue {coup_ia}")
            tour_humain = True

def jouer_mode_joueur():
    """
    Fonction qui lance une partie joueur contre joueur (JcJ)
    Retourne un tuple (resultat, mode, pseudo_joueur)
    Les deux joueurs alternent, on enregistre le pseudo du gagnant
    """
    reinitialiser_plateau()
    
    pseudo_joueur1 = input("\033[95m" + "Pseudo du joueur 1 (X) : " + "\033[0m").strip()
    if not pseudo_joueur1:
        pseudo_joueur1 = "Joueur1"
    
    pseudo_joueur2 = input("\033[95m" + "Pseudo du joueur 2 (O) : " + "\033[0m").strip()
    if not pseudo_joueur2:
        pseudo_joueur2 = "Joueur2"
    
    tour_joueur1 = True
    
    while True:
        utils.clear_console()
        print(affiche()[0])
        
        etat_actuel = plateau_en_liste(plateau)
        
        if verifier_gagnant(etat_actuel, HUMAIN):
            print(f"{pseudo_joueur1} (X) a gagné !")
            return ("victoire", pseudo_joueur1, pseudo_joueur2)
        
        if verifier_gagnant(etat_actuel, IA):
            print(f"{pseudo_joueur2} (O) a gagné !")
            return ("victoire", pseudo_joueur2, pseudo_joueur1)
        
        if not cases_libres(etat_actuel):
            print("Match nul !")
            return ("nul", pseudo_joueur1, pseudo_joueur2)
        
        if tour_joueur1:
            joueur_actuel = pseudo_joueur1
            symbole = HUMAIN
            print(f"Au tour de {joueur_actuel} (X)")
        else:
            joueur_actuel = pseudo_joueur2
            symbole = IA
            print(f"Au tour de {joueur_actuel} (O)")
        
        coup = input(f"{joueur_actuel}, votre coup : ").strip().upper()
        if point_setter(coup, symbole):
            tour_joueur1 = not tour_joueur1
        else:
            print("Coup invalide. Réessayez.")


def game_type_choice():
    """
        Fonction qui permet de choisir le mode de jeu (IA, Algorithmique ou JcJ)
        Retourne un tuple (resultat, mode, pseudo_joueur)
    """
    while True:
        print("Souhaitez vous jouer contre un joueur, un algorithme ou une IA (clé API Groq requise ❗)")
        choix = input("Votre choix (joueur / algo / ia) : ").strip().lower()

        if choix == "algo":
            pseudo_joueur = input("\033[95m" + "Entrez votre pseudo : " + "\033[0m").strip()
            if not pseudo_joueur:
                pseudo_joueur = "Joueur"
            return jouer_mode_algo(pseudo_joueur)
        elif choix == 'ia':
            pseudo_joueur = input("\033[95m" + "Entrez votre pseudo : " + "\033[0m").strip()
            if not pseudo_joueur:
                pseudo_joueur = "Joueur"
            return jouer_mode_ia(pseudo_joueur)
        elif choix == 'joueur':
            return jouer_mode_joueur()
        else:
            print("Choix invalide. Veuillez réessayer")

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
    pos = pos.strip().upper()
    if point_checker(pos):
        if plateau[int(pos[1]) - 1][ord(pos[0]) - ord("A")] == ".":
            plateau[int(pos[1]) - 1][ord(pos[0]) - ord("A")] = symbol
            return True
    return False