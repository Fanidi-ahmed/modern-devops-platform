# Bloc 01 — erreurs rencontrées

## Erreur
ModuleNotFoundError: No module named 'app'

## Contexte
Lancement de Uvicorn depuis le dossier `app/` avec :
`uvicorn app.src.main:app --reload`

## Cause probable
Le point de lancement ne correspondait pas au chemin d'import `app.src...`.

## Diagnostic
Python cherchait un package `app` alors que la commande était lancée depuis l'intérieur du dossier `app/`.

## Solution
Revenir à la racine du projet et lancer :
`uvicorn app.src.main:app --reload`

Ajout de fichiers `__init__.py` pour rendre la structure plus explicite.

## Ce que j'ai appris
Le dossier depuis lequel on lance l'application influence directement la résolution des imports Python.
