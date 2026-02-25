# 🖥️ Bash / Terminal Cheatsheet — PredictFlow

> Commandes apprises au fil de la formation. Mise à jour à chaque session.

---

## 🖥️ Terminal / PowerShell

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

## 🐍 Python

| Commande | Ce que ça fait |
|---|---|
| `python --version` | Vérifier la version Python |
| `python script.py` | Lancer un script Python |
| `python -c "code"` | Lancer du code Python directement (éviter sur PowerShell) |
| `python -m venv .venv` | Créer un environnement virtuel |
| `.venv\Scripts\activate` | Activer le venv (Windows) |
| `deactivate` | Désactiver le venv |

---

## 📦 pip / Packages

| Commande | Ce que ça fait |
|---|---|
| `pip --version` | Vérifier pip + voir quel venv est actif |
| `pip install <package>` | Installer une bibliothèque |
| `pip freeze > requirements.txt` | Sauvegarder toutes les dépendances |
| `pip install -r requirements.txt` | Réinstaller toutes les dépendances |

---

## 🔧 Git — Bases

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

---

## 🌿 Git — Branches & Merge

| Commande | Ce que ça fait |
|---|---|
| `git checkout -b <branch>` | Créer et switcher vers une nouvelle branche |
| `git checkout <branch>` | Switcher vers une branche existante |
| `git merge <branch>` | Merger une branche dans la branche courante |
| `git push origin <branch>` | Pousser une branche vers GitHub |
| `git branch -d <branch>` | Supprimer une branche locale |

---

## 🔍 Git — Historique & Diagnostic

| Commande | Ce que ça fait |
|---|---|
| `git log` | Voir l'historique détaillé |
| `git log --oneline` | Historique compact (1 ligne par commit) |
| `git log --oneline --graph --all` | Visualiser l'historique en arbre |
| `git diff` | Voir les modifications non committées |
| `git show HEAD` | Détails du dernier commit |
