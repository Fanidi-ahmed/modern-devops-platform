# App


Ce dossier contient l'application backend du projet.

## Structure

- `src/main.py` : point d'entrée FastAPI
- `src/config.py` : configuration de l'application
- `src/routes/` : endpoints HTTP
- `src/core/` : composants techniques transverses
- `tests/` : tests de l'application

## Lancer l'application

Depuis la racine du projet :

```bash
uvicorn app.src.main:app --reload