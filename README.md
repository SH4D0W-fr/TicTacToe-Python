# TicTacToe-Python 🎮

Une implémentation complète du jeu du Morpion (Tic-Tac-Toe) en Python avec interface en ligne de commande. Jouez contre une IA, un algorithme Minimax optimisé ou un autre joueur !

## 🌟 Fonctionnalités

- **3 modes de jeu** :
  - 👥 **Joueur vs Joueur** : Deux joueurs humains
  - 🤖 **Joueur vs Algorithme** : Jouez contre un algorithme Minimax invincible
  - 🧠 **Joueur vs IA Groq** : Affrontez une IA basée sur le modèle LLaMA 3.3-70B
  
- **Système de classement** : Suivi des statistiques des joueurs (victoires, défaites, nuls)
- **Sauvegarde persistante** : Les données des joueurs sont enregistrées dans un fichier CSV
- **Interface colorée** : Affichage amélioré avec codes couleur ANSI
- **Validation de coups** : Vérification automatique des mouvements valides

## 📋 Prérequis

- **Python 3.8+**
- **Connexion Internet** (pour le mode IA Groq)
- **Clé API Groq** (optionnelle, nécessaire seulement pour le mode IA)

## 🚀 Installation

### 1. Cloner le repository
```bash
git clone https://github.com/votre-pseudo/TicTacToe-Python.git
cd TicTacToe-Python
```

### 2. Créer un environnement virtuel (recommandé)
```bash
python -m venv venv
source venv/bin/activate  # Sur Windows: venv\Scripts\activate
```

### 3. Installer les dépendances
```bash
pip install -r requirements.txt
```

### 4. (Optionnel) Configurer la clé API Groq
Pour joueur contre l'IA, vous devez obtenir une clé API Groq :

1. Visitez [console.groq.com](https://console.groq.com)
2. Créez un compte et générez une clé API
3. À la première exécution, le programme vous demandera votre clé API
4. La clé sera sauvegardée dans un fichier `.env` pour une utilisation future

## 🎯 Comment jouer

### Démarrer le jeu
```bash
python main.py
```

### Menu principal
Le jeu affiche un menu avec 3 options :
1. **Jouer** : Lance une partie avec votre mode préféré
2. **Classement** : Affiche le classement global des joueurs
3. **Quitter** : Quitter le jeu

### Coordonnées du plateau
Le plateau est numéroté comme suit :
```
    A B C
  1 . . .
  2 . . .
  3 . . .
```

**Exemples de coups valides** : `A1`, `B2`, `C3`

### Modes de jeu détaillés

#### Mode Joueur vs Joueur
- Deux joueurs alternent leurs coups
- Joueur 1 utilise le symbole `X`
- Joueur 2 utilise le symbole `O`
- Les noms des joueurs sont enregistrés dans le classement

#### Mode Joueur vs Algorithme
- Vous jouez contre un algorithme Minimax parfait
- L'algorithme ne peut jamais perdre (victoire ou nul)
- Utilisé pour tester les stratégies de jeu

#### Mode Joueur vs IA
- Vous jouez contre une IA basée sur le modèle LLaMA 3.3-70B de Groq
- L'IA prend ses décisions via une API distante
- Dispose d'une logique stratégique mais reste battable

## 🏗️ Architecture du projet

```
TicTacToe-Python/
├── main.py                 # Point d'entrée du programme
├── requirements.txt        # Dépendances Python
├── data.csv               # Base de données des joueurs
├── .env                   # Variables d'environnement (créé à l'exécution)
├── LICENSE                # Licence du projet
├── README.md              # Documentation
└── modules/
    ├── __init__.py
    ├── game_manager.py    # Logique principale du jeu
    ├── ai_manager.py      # Gestion de l'IA Groq
    ├── save_manager.py    # Gestion de la base de données CSV
    ├── leaderboard_manager.py  # Affichage du classement
    └── utils.py           # Fonctions utilitaires
```

## 📦 Modules détaillés

### `game_manager.py`
Gère la logique du jeu :
- **`reinitialiser_plateau()`** : Réinitialise le plateau de jeu
- **`affiche()`** : Affiche le plateau avec coordonnées
- **`point_checker()`** : Valide une position (ex: "A1")
- **`point_setter()`** : Place un symbole sur le plateau
- **`verifier_gagnant()`** : Vérifie si un joueur a gagné
- **`cases_libres()`** : Récupère les cases disponibles
- **`minimax()`** : Algorithme Minimax récursif
- **`meilleur_coup()`** : Calcule le coup optimal
- **`jouer_mode_algo()`** : Lance une partie contre l'algorithme
- **`jouer_mode_ia()`** : Lance une partie contre l'IA Groq
- **`jouer_mode_joueur()`** : Lance une partie joueur vs joueur
- **`game_type_choice()`** : Menu de sélection du mode de jeu

### `ai_manager.py`
Gère la communication avec l'API Groq :
- **`get_key()`** : Récupère ou demande la clé API
- **`validate_api_key()`** : Valide la clé API
- **`get_client()`** : Initialise le client Groq
- **`ai_play()`** : Demande le prochain coup à l'IA

### `save_manager.py`
Gère la persistance des données :
- **`initialiser_csv()`** : Crée le fichier data.csv
- **`ajouter_ou_mettre_a_jour()`** : Enregistre/met à jour un joueur
- **`lire_tous_joueurs()`** : Récupère tous les joueurs
- **`obtenir_stats_joueur()`** : Récupère les stats d'un joueur
- **`ecrire_donnees()`** : Écrit les données dans le CSV
- **`trier_classement()`** : Trie les joueurs (victoires > nuls > défaites)
- **`obtenir_classement()`** : Retourne le classement global

### `leaderboard_manager.py`
Affiche les statistiques :
- **`afficher_classement()`** : Affiche le classement global
- **`afficher_stats_joueur()`** : Affiche les stats d'un joueur spécifique

### `utils.py`
Fonctions utilitaires :
- **`clear_console()`** : Efface l'écran
- **`set_env()`** : Crée/modifie une variable d'environnement
- **`get_env()`** : Récupère une variable d'environnement

## 🧮 Algorithmes

### Minimax
L'algorithme Minimax parcourt tous les coups possibles de manière récursive :
- **Score 1** : L'IA gagne
- **Score -1** : Le joueur humain gagne
- **Score 0** : Match nul

Le joueur qui maximise cherche le meilleur score pour l'IA, tandis que celui qui minimise cherche à réduire les chances de l'IA.

### Conversion indice ↔ position
- Position → Indice : `ligne = (pos[1] - 1), colonne = ord(pos[0]) - ord("A")`
- Indice → Position : `indice = ligne * 3 + colonne` → `f"{chr(65 + col)}{ligne + 1}"`

## 📊 Format de la base de données

Le fichier `data.csv` utilise le format suivant :
```csv
pseudo;victoires;défaites;nuls
Alice;5;1;2
Bob;3;2;4
```

Les joueurs sont triés automatiquement par :
1. Nombre de victoires (décroissant)
2. Nombre de nuls (décroissant)
3. Nombre de défaites (croissant)

## 🔒 Sécurité

- La clé API Groq est stockée localement dans un fichier `.env`
- Ce fichier **ne doit pas être versionné** (il est ignoré par `.gitignore`)
- Les données des joueurs sont publiques (CSV sans chiffrement)

## 🐛 Dépannage

### "Aucune clé API enregistrée"
- Vous avez sélectionné le mode IA mais aucune clé n'existe
- Visitez [console.groq.com](https://console.groq.com) pour en créer une

### "Clé API invalide"
- Votre clé a expiré ou est incorrecte
- Supprimez le fichier `.env` et relancez le jeu

### "Erreur de connexion à Groq"
- Vérifiez votre connexion Internet
- Vérifiez que vous disposez de crédits API Groq

## 🎓 Apprentissages clés

Ce projet démontre :
- ✅ Programmation modulaire avec plusieurs fichiers
- ✅ Algorithmes récursifs (Minimax)
- ✅ Gestion de fichiers (CSV)
- ✅ Intégration API (Groq)
- ✅ Variables d'environnement
- ✅ Interface ligne de commande interactive
- ✅ Gestion des exceptions
- ✅ Systèmes de classement et statistiques

## 📄 Licence

Ce projet est sous licence [MIT](LICENSE). Vous êtes libre de le modifier et le distribuer.

## 🤝 Contribution

Les contributions sont bienvenues ! N'hésitez pas à :
- 🐛 Signaler des bugs
- 💡 Proposer des améliorations
- 📚 Améliorer la documentation

## 📧 Support

Pour toute question ou problème, ouvrez une issue sur le repository.
