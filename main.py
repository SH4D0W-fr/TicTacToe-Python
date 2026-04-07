plateau = [[".", ".", "."], [".", ".", "."], [".", ".", "."]]

def affiche():
	""" 
		Affiche le plateau de jeu dans la console de manière lisible
	"""
	print("\t \t", "  0 1 2")
	for j in range(len(plateau)):
		print("\t \t", j, end=" ")
		for i in range(len(plateau[0]) - 1):
			print(plateau[j][i], end=" ")
		print(plateau[j][-1])


if __name__ == "__main__":	
	"""
		Ici vos procédures de test.
		Si vous créez un module, et que vous importez ce fichier 
		dans un autre script, ces procédures ne seront pas exécutées
	"""
	affiche()