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


def afficher_stats_joueur(pseudo: str):
    """
    Affiche les stats détaillées d'un joueur
    """
    stats = save_manager.obtenir_stats_joueur(pseudo)
    
    if not stats:
        print(f"\033[91m" + f"Joueur '{pseudo}' non trouvé." + "\033[0m")
        return
    
    print("\n" + "\033[1m" + "\033[94m" + "═" * 60 + "\033[0m")
    print("\033[1m" + "\033[94m" + f"Stats de {pseudo:^50}" + "\033[0m")
    print("\033[1m" + "\033[94m" + "═" * 60 + "\033[0m\n")
    
    victoires = int(stats.get("victoires", 0))
    defaites = int(stats.get("défaites", 0))
    nuls = int(stats.get("nuls", 0))
    
    total = victoires + defaites + nuls
    
    print(f"  Victoires : {victoires}")
    print(f"  Défaites  : {defaites}")
    print(f"  Nuls      : {nuls}")
    
    if total > 0:
        taux_victoire = (victoires / total) * 100
        print(f"  Taux de victoire : {taux_victoire:.1f}%")
    
    print("\033[1m" + "\033[94m" + "═" * 60 + "\033[0m\n")
