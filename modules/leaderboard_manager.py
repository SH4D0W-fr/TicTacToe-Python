import modules.save_manager as save_manager


def afficher_classement():
    """
    Affiche le classement des joueurs
    """
    classement = save_manager.obtenir_classement()
    
    if not classement:
        print("\033[93m" + "Aucun joueur enregistré pour le moment." + "\033[0m")
        return
    
    print("\n" + "\033[1m" + "\033[94m" + "═" * 60 + "\033[0m")
    print("\033[1m" + "\033[94m" + f"{'Classement Global':^60}" + "\033[0m")
    print("\033[1m" + "\033[94m" + "═" * 60 + "\033[0m\n")
    
    # En-tête
    print(f"{'Rang':<5} {'Pseudo':<20} {'Victoires':<12} {'Défaites':<12} {'Nuls':<12}")
    print("-" * 60)
    
    # Afficher les joueurs
    for rang, joueur in enumerate(classement, 1):
        pseudo = joueur["pseudo"]
        victoires = joueur.get("victoires", 0)
        defaites = joueur.get("défaites", 0)
        nuls = joueur.get("nuls", 0)
        
        couleur = "\033[92m" if rang == 1 else ""
        reset = "\033[0m" if rang == 1 else ""
        
        print(f"{couleur}{rang:<5} {pseudo:<20} {victoires:<12} {defaites:<12} {nuls:<12}{reset}")
    
    print("\n" + "\033[1m" + "\033[94m" + "═" * 60 + "\033[0m\n")
