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
		resultat_partie, mode, pseudo_joueur = resultat
		# Pour le mode joueur, on doit enregistrer les stats pour les deux joueurs
		# Mais on ne reçoit que le pseudo du gagnant (ou joueur1 en cas de nul)
		save_manager.ajouter_ou_mettre_a_jour(pseudo_joueur, resultat_partie, mode)
		print(f"\n\033[92m" + f"✓ Stats enregistrées pour {pseudo_joueur}" + "\033[0m\n")
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
	menu_principal()