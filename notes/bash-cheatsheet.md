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
| git --version | Vérifier que Git est installé | `git --version` |
| git add . | Préparer tous les fichiers | `git add .` |
| git commit -m | Enregistrer une version | `git commit -m "feat: ..."` |
| git config --global | Régler nom et email (une fois) | `git config --global user.name "Nom"` |
| git init | Créer un dépôt | `git init` |
| git push -u origin main | Envoyer vers GitHub et mémoriser le lien | `git push -u origin main` |
| git remote add origin | Relier le dépôt local à GitHub | `git remote add origin URL` |

## Git-Branches
| Commande | Rôle | Exemple |
|---|---|---|
| git branch -M main | Renommer la branche en main | `git branch -M main` |

## Git-Diag
| Commande | Rôle | Exemple |
|---|---|---|
| git log --oneline | Historique résumé (hash + message) | `git log --oneline` |
| git status | Voir l'état du dépôt | `git status` |

## Glossaire Python
| Notion | Exemple |
|---|---|
| with open | `with open(CHEMIN, "r", encoding="utf-8") as f:` |
| readline() / readlines() | Une ligne / toutes les lignes |
| strip() / split(",") | Nettoyer / découper |
| liste[-1] | Dernier élément |
| liste[1:] | À partir de l'indice 1 |