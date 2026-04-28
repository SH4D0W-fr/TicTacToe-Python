import modules.utils as utils
import modules.game_manager as game_manager
import modules.ai_manager as ai_manager
import modules.save_manager as save_manager
import modules.leaderboard_manager as leaderboard_manager

def lancer_partie():
	"""
	Lance une partie avec choix du mode et des pseudos
	"""
	resultat = game_manager.game_type_choice()
	if resultat:
		resultat_partie, gagnant, perdant = resultat
		# Pour le mode joueur, on doit enregistrer les stats pour les deux joueurs
		if resultat_partie == "victoire":
			save_manager.ajouter_ou_mettre_a_jour(gagnant, "victoire")
			save_manager.ajouter_ou_mettre_a_jour(perdant, "défaite")
		elif resultat_partie == "nul":
			save_manager.ajouter_ou_mettre_a_jour(gagnant, "nul")
			save_manager.ajouter_ou_mettre_a_jour(perdant, "nul")
		print(f"\n\033[92m" + f"✓ Stats enregistrées pour {gagnant} et {perdant}" + "\033[0m\n")
		input("Appuyez sur Entrée pour continuer...")
	menu_principal()

def menu_principal():
	"""
	Menu principal avec toutes les options possibles pour le jeu
	"""
	
	utils.clear_console()
	
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
	print("\033[94m" + "Options :" + "\033[0m")
	print("\033[95m" + "1 : Jouer" + "\033[0m")
	print("\033[92m" + "2 : Classement" + "\033[0m")
	print("\033[93m" + "3 : Quitter" + "\033[0m")
	# Les codes correspondent aux effets sur le texte (couleur et gras)
	def selection():
		choix = input("\nVotre choix : ")
		if choix == "1":
			lancer_partie()
		elif choix == "2":
			utils.clear_console()
			leaderboard_manager.afficher_classement()
			input("Appuyez sur Entrée pour continuer...")
			menu_principal()
		elif choix == "3":
			utils.clear_console()
			print("\033[92m" + "À bientôt !" + "\033[0m")
			return
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

	# utils.clear_console()
	# print(game_manager.point_setter("A1", "X")) # Test de placement d'un point valide
	# print(game_manager.point_setter("A1", "O")) # Test de placement d'un point déjà occupé
	# print(game_manager.point_setter("E4", "X")) # Test de placement d'un point invalide
	# print(game_manager.affiche()[0]) # Affichage du plateau après les placements
	
	# utils.clear_console()
	# choix_ia = ai_manager.ai_play(game_manager.affiche()[1])
	# print(choix_ia) # Test de l'IA pour jouer un coup
	# print(game_manager.point_setter(choix_ia, "O")) # Placement du coup de l'IA
	# print(game_manager.affiche()[0]) # Affichage du plateau après le coup de l'IA
	# print(game_manager.win_condition(game_manager.affiche()[1], "X")) # Fonction changée
	# test_plateau = [["X", ".", "."], [".", "X", "."], [".", ".", "X"]]
	# print(game_manager.win_condition(test_plateau, "X")) # Fonction changée

	menu_principal()