# Image de base
FROM python:3.11-slim

# Dossier de travail dans le conteneur
WORKDIR /app

# Copier les dépendances
COPY app/requirements.txt .

# Installer les dépendances
RUN pip install --no-cache-dir -r requirements.txt

# Copier le code
COPY app ./app

# Exposer le port
EXPOSE 8000

# Commande de lancement
CMD ["uvicorn", "app.src.main:app", "--host", "0.0.0.0", "--port", "8000"]