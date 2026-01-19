# 1. Image de base
FROM python:3.11-slim

# 2. Créer le dossier de travail
WORKDIR /app

# 3. Copier requirements et installer
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# 4. Copier le reste du code
COPY . .

# 5. Exposer le port
EXPOSE 8000

# 6. Lancer le serveur
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
