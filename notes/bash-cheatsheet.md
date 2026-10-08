# Bash / PowerShell cheatsheet

## Terminal
| Commande | Rôle | Exemple |
|---|---|---|
| cd | Changer de dossier | `cd predictflow` |
| cd .. | Remonter au dossier parent | `cd ..` |
| dir | Lister le contenu du dossier | `dir data` |
| mkdir | Créer un dossier | `mkdir data, src` |
| Move-Item | Déplacer ou renommer | `Move-Item a.md notes\b.md` |
| New-Item | Créer un fichier | `New-Item README.md -ItemType File` |
| tree /F | Afficher l'arborescence | `tree /F` |

## Python
| Commande | Rôle | Exemple |
|---|---|---|
| python --version | Version installée | `python --version` |
| python -m venv venv | Créer l'environnement virtuel | `python -m venv venv` |
| venv\Scripts\activate | Activer le venv (Windows) | `venv\Scripts\activate` |
| python fichier.py | Exécuter un script | `python src\loader.py` |

## pip
| Commande | Rôle | Exemple |
|---|---|---|
| pip list | Voir les paquets installés | `pip list` |

## Git-Bases
| Commande | Rôle | Exemple |
|---|---|---|
| git init | Créer un dépôt | `git init` |
| git status | Voir l'état du dépôt | `git status` |
| git add . | Préparer tous les fichiers | `git add .` |
| git commit -m | Enregistrer une version | `git commit -m "feat: ..."` |

## Glossaire Python
| Notion | Exemple |
|---|---|
| with open | `with open(CHEMIN, "r", encoding="utf-8") as f:` |
| readline() / readlines() | Une ligne / toutes les lignes |
| strip() / split(",") | Nettoyer / découper |
| liste[-1] | Dernier élément |
| liste[1:] | À partir de l'indice 1 |