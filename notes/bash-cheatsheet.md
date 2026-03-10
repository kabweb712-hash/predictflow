# 🖥️ Bash / Terminal Cheatsheet — PredictFlow

> Commandes apprises au fil de la formation. Mise à jour à chaque session.

---

## 1. 🖥️ Terminal / PowerShell

| Commande | Ce que ça fait |
|---|---|
| `cd C:\Users\hossk` | Aller à un dossier |
| `cd ..` | Remonter d'un niveau |
| `ls` | Lister le contenu du dossier |
| `pwd` | Afficher le chemin actuel |
| `mkdir nom-dossier` | Créer un dossier |
| `mkdir a, b, c` | Créer plusieurs dossiers d'un coup |
| `New-Item fichier.txt -type file` | Créer un fichier vide |
| `Rename-Item ancien nouveau` | Renommer un fichier/dossier |
| `code fichier.py` | Ouvrir un fichier dans VS Code |
| `code .` | Ouvrir tout le dossier dans VS Code |
| `q` | Quitter le pager `less` dans le terminal |

---

## 2. 🐍 Python

| Commande | Ce que ça fait |
|---|---|
| `python --version` | Vérifier la version Python |
| `python script.py` | Lancer un script Python |
| `python src/script.py` | Lancer un script depuis un sous-dossier |
| `python -c "code"` | Lancer du code Python directement (éviter sur PowerShell) |
| `python -m venv .venv` | Créer un environnement virtuel |
| `.venv\Scripts\activate` | Activer le venv (Windows) |
| `deactivate` | Désactiver le venv |
| `python -m module.name` | Exécuter un module Python (gère les imports relatifs) |
| `python script.py` |	Exécuter un script Python directement |

---

## 3. 📦 pip / Packages

| Commande | Ce que ça fait |
|---|---|
| `pip --version` | Vérifier pip + voir quel venv est actif |
| `pip install <package>` | Installer une bibliothèque |
| `pip freeze > requirements.txt` | Sauvegarder toutes les dépendances |
| `pip install -r requirements.txt` | Réinstaller toutes les dépendances |

---

## 4. 🔧 Git — Bases

| Commande | Ce que ça fait |
|---|---|
| `git --version` | Vérifier Git |
| `git config --global user.name` | Voir/définir ton nom |
| `git config --global user.email` | Voir/définir ton email |
| `git init` | Initialiser un repo Git |
| `git status` | Voir l'état des fichiers |
| `git add .` | Ajouter tous les fichiers au staging |
| `git add fichier.py` | Ajouter un fichier spécifique |
| `git commit -m "message"` | Sauvegarder un snapshot |
| `git remote add origin URL` | Relier au repo GitHub |
| `git branch -M main` | Renommer la branche en main |
| `git push -u origin main` | Envoyer sur GitHub (1ère fois) |
| `git push` | Envoyer sur GitHub (fois suivantes) |
| `git pull` | Récupérer les modifications depuis GitHub |

---

## 5. 🌿 Git — Branches & Merge

| Commande | Ce que ça fait |
|---|---|
| `git checkout -b <branch>` | Créer et switcher vers une nouvelle branche |
| `git checkout <branch>` | Switcher vers une branche existante |
| `git merge <branch>` | Merger une branche dans la branche courante |
| `git push origin <branch>` | Pousser une branche vers GitHub |
| `git branch -d <branch>` | Supprimer une branche locale |

---

## 6. 🔍 Git — Historique & Diagnostic

| Commande | Ce que ça fait |
|---|---|
| `git log` | Voir l'historique détaillé |
| `git log --oneline` | Historique compact (1 ligne par commit) |
| `git log --oneline --graph --all` | Visualiser l'historique en arbre |
| `git diff` | Voir les modifications non committées |
| `git show HEAD` | Détails du dernier commit |

---

## 7. 📚 Glossaire Python

| Terme | Définition | Exemple |
|---|---|---|
| `str` | String — chaîne de texte | `"Alice"`, `"Month-to-month"` |
| `int` | Integer — nombre entier | `42`, `12`, `-5` |
| `float` | Nombre décimal (virgule) | `42.7`, `0.6` |
| `bool` | Booléen — vrai ou faux | `True`, `False` |
| `list` | Liste ordonnée, modifiable, doublons OK | `[1, 2, 2, 3]` |
| `tuple` | Liste immuable (non modifiable après création) | `(1, 2, 3)` |
| `set` | Ensemble sans doublons, non ordonné | `{1, 2, 3}` |
| `dict` | Dictionnaire clé:valeur | `{"nom": "Alice", "age": 30}` |
| `type hint` | Annotation du type attendu d'une variable/fonction | `def f(x: str) -> int:` |
| `DataFrame` | Tableau de données Pandas (lignes + colonnes) | `pd.read_csv("data.csv")` |
| `mask` | Série de True/False pour filtrer un DataFrame | `df[mask]` |
| `list comprehension` | Boucle `for` + `if` condensée en 1 ligne | `[x for x in l if x > 0]` |
| `generator` | Comme list comprehension mais calcul à la demande | `(x for x in l if x > 0)` |
| `logging` | Module Python pour tracer l'exécution d'un programme | `import logging` |
| `Logger` | Objet qui enregistre les messages de log | `logger = logging.getLogger("nom")` |
| `Handler` | Destination des logs (console, fichier, etc.) | `StreamHandler`, `FileHandler` |
| `Formatter` | Définit le format d'affichage des logs | `'%(asctime)s - %(levelname)s'` |
| `DEBUG` | Niveau de log : détails techniques (développement) | `logger.debug("détail")` |
| `INFO` | Niveau de log : déroulement normal du programme | `logger.info("OK")` |
| `WARNING` | Niveau de log : problème non-bloquant à surveiller | `logger.warning("attention")` |
| `ERROR` | Niveau de log : erreur empêchant une opération | `logger.error("échec")` |
| `CRITICAL` | Niveau de log : erreur grave nécessitant l'arrêt | `logger.critical("crash")` |

---

## 8. 🐼 Pandas — Manipulation de données

| Commande | Ce que ça fait |
|---|---|
| `pd.read_csv('path/file.csv')` | Charger un fichier CSV dans un DataFrame |
| `df.dtypes` | Afficher le type de chaque colonne |
| `df.shape` | Afficher (nb_lignes, nb_colonnes) |
| `df.drop(columns=['col'])` | Supprimer une ou plusieurs colonnes |
| `pd.to_numeric(df['col'], errors='coerce')` | Convertir en nombre, invalides → NaN |
| `df['col'].isna().sum()` | Compter les NaN d'une colonne |
| `df.isnull().sum().sum()` | Compter tous les NaN du DataFrame |
| `df.dropna()` | Supprimer les lignes contenant des NaN |
| `df['col'].map({'Yes': 1, 'No': 0})` | Remplacer des valeurs selon un dictionnaire |
| `df['col'].unique()` | Afficher les valeurs uniques d'une colonne |
| `Move-Item src dst` | Déplacer un fichier (PowerShell) |


