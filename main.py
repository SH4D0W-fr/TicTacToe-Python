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

def menu_principal():
	"""
	Menu principal avec toutes les options possibles pour le jeu
	"""
	print("Morpion")
	print("Bienvenue sur le jeu !")
	print("Options :")
	print("1 : Jouer")
	print("2 : Classement")
	print("3 : Crédits")
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
	affiche() # Test du plateau vide
	menu_principal()