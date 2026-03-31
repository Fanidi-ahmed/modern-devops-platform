# Bloc 01 — API backend

## But du bloc

Créer une structure propre pour une API FastAPI dès le départ.

## Ce que j'apprends

- rôle du point d'entrée `main.py`
- intérêt d'une configuration centralisée avec `config.py`
- séparation entre routes et logique technique
- importance du point de lancement dans les imports Python
- intérêt du logging dès le début

## Structure mise en place

- `main.py` : crée l'application FastAPI
- `config.py` : lit la configuration depuis l'environnement
- `routes/health.py` : endpoint de santé
- `core/logging.py` : base du logging applicatif
- `tests/` : préparation pour les tests futurs

## Endpoint disponible

- `GET /health` → retourne `{"status": "ok"}`

## Ce que je dois retenir

- ne pas tout mettre dans `main.py`
- préparer la structure avant que le projet grossisse
- lancer Uvicorn depuis la racine du projet si les imports utilisent `app.src...`