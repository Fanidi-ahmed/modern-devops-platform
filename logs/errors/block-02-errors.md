## Erreur
ImportError: email-validator is not installed

## Contexte
Utilisation de EmailStr dans un modèle Pydantic

## Cause probable
Le type EmailStr nécessite la dépendance externe email-validator

## Diagnostic
Pydantic utilise des dépendances optionnelles pour certains types avancés

## Solution
Installer la dépendance :
pip install email-validator

Ajouter dans requirements.txt :
email-validator

## Ce que j'ai appris
Certains types Pydantic nécessitent des dépendances supplémentaires