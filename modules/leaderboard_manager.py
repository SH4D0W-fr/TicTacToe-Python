import modules.save_manager as save_manager


def afficher_classement(mode: str = None):
    """
    Affiche le classement des joueurs
    mode: "algo", "ia" ou None (tous)
    """
    classement = save_manager.obtenir_classement(mode)
    
    if not classement:
        print("\033[93m" + "Aucun joueur enregistré pour le moment." + "\033[0m")
        return
    
    print("\n" + "\033[1m" + "\033[94m" + "═" * 60 + "\033[0m")
    
    if mode == "algo":
        titre = "Classement - Mode Algorithme"
    elif mode == "ia":
        titre = "Classement - Mode IA"
    else:
        titre = "Classement Global"
    
    print("\033[1m" + "\033[94m" + f"{titre:^60}" + "\033[0m")
    print("\033[1m" + "\033[94m" + "═" * 60 + "\033[0m\n")
    
    # En-tête
    print(f"{'Rang':<5} {'Pseudo':<20} {'Victoires':<12} {'Défaites':<12} {'Nuls':<12}")
    print("-" * 60)
    
    # Afficher les joueurs
    for rang, joueur in enumerate(classement, 1):
        pseudo = joueur["pseudo"]
        
        if mode == "algo":
            victoires = joueur.get("victoires_algo", 0)
            defaites = joueur.get("défaites_algo", 0)
            nuls = joueur.get("nuls_algo", 0)
        elif mode == "ia":
            victoires = joueur.get("victoires_ia", 0)
            defaites = joueur.get("défaites_ia", 0)
            nuls = joueur.get("nuls_ia", 0)
        else:
            victoires = int(joueur.get("victoires_algo", 0)) + int(joueur.get("victoires_ia", 0))
            defaites = int(joueur.get("défaites_algo", 0)) + int(joueur.get("défaites_ia", 0))
            nuls = int(joueur.get("nuls_algo", 0)) + int(joueur.get("nuls_ia", 0))
        
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
    
    victoires_algo = int(stats.get("victoires_algo", 0))
    defaites_algo = int(stats.get("défaites_algo", 0))
    nuls_algo = int(stats.get("nuls_algo", 0))
    
    victoires_ia = int(stats.get("victoires_ia", 0))
    defaites_ia = int(stats.get("défaites_ia", 0))
    nuls_ia = int(stats.get("nuls_ia", 0))
    
    total_algo = victoires_algo + defaites_algo + nuls_algo
    total_ia = victoires_ia + defaites_ia + nuls_ia
    
    print("\033[95m" + "Mode Algorithme :" + "\033[0m")
    print(f"  Victoires : {victoires_algo}")
    print(f"  Défaites  : {defaites_algo}")
    print(f"  Nuls      : {nuls_algo}")
    if total_algo > 0:
        taux_victoire = (victoires_algo / total_algo) * 100
        print(f"  Taux de victoire : {taux_victoire:.1f}%")
    
    print("\n\033[96m" + "Mode IA :" + "\033[0m")
    print(f"  Victoires : {victoires_ia}")
    print(f"  Défaites  : {defaites_ia}")
    print(f"  Nuls      : {nuls_ia}")
    if total_ia > 0:
        taux_victoire = (victoires_ia / total_ia) * 100
        print(f"  Taux de victoire : {taux_victoire:.1f}%")
    
    total = victoires_algo + victoires_ia
    print("\n\033[92m" + f"Total des victoires : {total}" + "\033[0m")
    print("\033[1m" + "\033[94m" + "═" * 60 + "\033[0m\n")
