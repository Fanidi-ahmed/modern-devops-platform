# Bloc 03 — PostgreSQL et persistance

## But du bloc

Remplacer le stockage en mémoire par une vraie base PostgreSQL et apprendre la persistance réelle.

## Ce que j'apprends

- différence entre mémoire applicative et persistance
- rôle de SQLAlchemy
- rôle de l'engine, de la session et de Base
- rôle d'un modèle ORM
- lien entre FastAPI, service, session DB et PostgreSQL
- gestion d'une contrainte unique avec rollback et HTTP 409

## Structure

- `database.py` : engine, session, Base, get_db
- `models/user.py` : modèle SQLAlchemy
- `services/user_service.py` : logique DB
- `routes/users.py` : injection de session et réponses HTTP

## Ce que je dois retenir

- une liste Python n'est pas une base de données
- une vraie DB survit au redémarrage de l'API
- une transaction qui échoue doit faire rollback
- une erreur SQL prévue doit être transformée en réponse API propre