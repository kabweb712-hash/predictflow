🖥️ Terminal / PowerShell

Commande	Ce que ça fait

cd C:\\Users\\hossk	Aller à un dossier

cd ..	Remonter d'un niveau

mkdir nom-dossier	Créer un dossier

mkdir a, b, c	Créer plusieurs dossiers d'un coup

Rename-Item ancien nouveau	Renommer un fichier/dossier

New-Item fichier.txt -type file	Créer un fichier vide

ls	Lister le contenu du dossier

pwd	Afficher le chemin actuel

code fichier.py	Ouvrir un fichier dans VS Code

code .	Ouvrir tout le dossier dans VS Code



🐍 Python / venv

Commande	Ce que ça fait

python --version	Vérifier la version Python

pip --version	Vérifier pip + voir quel venv est actif

python -m venv .venv	Créer un environnement virtuel

.venv\\Scripts\\activate	Activer le venv

deactivate	Désactiver le venv

python script.py	Lancer un script Python



🔧 Git

Commande	Ce que ça fait

git --version	Vérifier Git

git config --global user.name	Voir ton nom configuré

git config --global user.email	Voir ton email configuré

git init	Initialiser un repo Git

git add .	Ajouter tous les fichiers au staging

git status	Voir l'état des fichiers

git commit -m "message"	Sauvegarder un snapshot

git remote add origin URL	Relier au repo GitHub

git branch -M main	Renommer la branche en main

git push -u origin main	Envoyer sur GitHub (1ère fois)

git push	Envoyer sur GitHub (fois suivantes)





\## 📦 pip / Packages



| Commande | Ce que ça fait |

|---|---|

| `pip install <package>` | Installer une bibliothèque dans le venv |

| `pip install pandas` | Installer pandas (bibliothèque data science) |

| `pip freeze > requirements.txt` | Sauvegarder toutes les dépendances du projet |

| `pip install -r requirements.txt` | Réinstaller toutes les dépendances depuis le fichier |



\## 🔧 Git — Historique \& Navigation



| Commande | Ce que ça fait |

|---|---|

| `git log --oneline` | Voir l'historique des commits (1 ligne par commit) |

| `git log` | Voir l'historique détaillé des commits |



\## 🐍 Python — Exécution



| Commande | Ce que ça fait |

|---|---|

| `python test\_loader.py` | Lancer un script Python spécifique |

| `python -c "code"` | Lancer du code Python directement (éviter sur PowerShell) |



