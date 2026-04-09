import modules.game_manager as game_manager

def menu_principal():
	"""
	Menu principal avec toutes les options possibles pour le jeu
	"""
	print("\033[91m" + r"""
		*        )   (    (    (        )      )  
		(  `    ( /(   )\ ) )\ ) )\ )  ( /(   ( /(  
		)\))(   )\()) (()/((()/((()/(  )\())  )\()) 
		((_)()\ ((_)\   /(_))/(_))/(_))((_)\  ((_)\  
		(_()((_)  ((_) (_)) (_)) (_))    ((_)  _((_) 
		|  \/  | / _ \ | _ \| _ \|_ _|  / _ \ | \| | 
		| |\/| || (_) ||   /|  _/ | |  | (_) || .` | 
		|_|  |_| \___/ |_|_\|_|  |___|  \___/ |_|\_| 																													
	""" + "\033[0m")
	print("\033[1m" + "\033[94m" + "Bienvenue sur le jeu !" + "\033[0m")
	print("\033[94m" + "Options :" + "\033[0m")
	print("\033[95m" + "1 : Jouer" + "\033[0m")
	print("\033[92m" + "2 : Classement" + "\033[0m")
	print("\033[93m" + "3 : Crédits" + "\033[0m")
	# Les codes correspondent aux effets sur le texte (couleur et gras)
	def selection():
		choix = input("Votre choix : ")
		if choix == "1":
			a = 0
			# Appel fonction pour jouer
		elif choix == "2":
			a = 0
			# Appel fonction classement
		elif choix == "3":
			a = 0
			# Appel fonction crédits
		else:
			print("Choix invalide")
			selection()
	selection()


if __name__ == "__main__":	
	"""
		Ici vos procédures de test.
		Si vous créez un module, et que vous importez ce fichier 
		dans un autre script, ces procédures ne seront pas exécutées
	"""
	# print(game_manager.affiche()[0]) # Test du plateau vide ([0] car la fonction affiche() retourne une str et une list, on veut juste la str)
	# menu_principal() # Test du menu principal
	# print(game_manager.point_checker("A1")) # Test d'un point valide
	# print(game_manager.point_checker("E4")) # Test d'un point invalide

	print(game_manager.point_setter("A1", "X")) # Test de placement d'un point valide
	print(game_manager.point_setter("A1", "O")) # Test de placement d'un point déjà occupé
	print(game_manager.point_setter("E4", "X")) # Test de placement d'un point invalide
	print(game_manager.affiche()[0]) # Affichage du plateau après les placements