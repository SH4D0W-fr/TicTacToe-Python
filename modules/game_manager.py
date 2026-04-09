def affiche():
	"""
		Affiche le plateau de jeu dans la console de manière lisible
		Code fourni
	"""
	plateau = [[".", ".", "."], [".", ".", "."], [".", ".", "."]]
	print("\t \t", "  0 1 2")
	for j in range(len(plateau)):
		print("\t \t", j, end=" ")
		for i in range(len(plateau[0]) - 1):
			print(plateau[j][i], end=" ")
		print(plateau[j][-1])

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
