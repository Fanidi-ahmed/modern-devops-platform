# Bloc 00 — erreurs rencontrées

## Format à utiliser

### Erreur
Message exact :

### Contexte
Commande lancée :

### Cause probable
...

### Diagnostic
...

### Solution
...

### Ce que j'ai appris
...
## Erreur
ModuleNotFoundError: No module named 'app'

## Contexte
Lancement de uvicorn depuis le dossier `app/` avec la commande :
`uvicorn app.src.main:app --reload`

## Cause probable
Le dossier courant était `app/`, donc Python ne voyait pas le package racine `app`.

## Diagnostic
Les imports utilisaient `from app.src...`, ce qui suppose un lancement depuis la racine du projet.

## Solution
Revenir à la racine `modern-devops-platform/` puis lancer :
`uvicorn app.src.main:app --reload`

Ajout de fichiers `__init__.py` pour clarifier la structure des packages.

## Ce que j'ai appris
Le point de lancement influence directement la résolution des imports Python.