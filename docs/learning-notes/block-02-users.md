# Bloc 02 — Route, schéma, service

## But du bloc

Créer un mini flux backend propre avec création et lecture d'utilisateurs sans base de données.

## Ce que j'apprends

- rôle d'une route FastAPI
- rôle d'un schéma Pydantic
- rôle d'un service métier
- différence entre données d'entrée et données de sortie
- validation automatique d'un email avec EmailStr

## Structure

- `routes/users.py` : endpoints `/users`
- `schemas/user.py` : validation et structure des données
- `services/user_service.py` : logique métier simple en mémoire

## Ce que je dois retenir

- la route orchestre
- le service exécute la logique
- le schéma définit le contrat d'entrée/sortie
- un backend propre sépare ses responsabilités