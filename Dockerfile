# Image de base Python
FROM python:3.9-slim

# Definir le repertoire de travail
WORKDIR /app

# Copier les fichiers de dependances
COPY requirements.txt .

# Installer les dependances
RUN pip install --no-cache-dir -r requirements.txt

# Copier le code source
COPY src/ ./src/
COPY config/ ./config/
COPY models/ ./models/

# Creer les dossiers necessaires
RUN mkdir -p logs data

# Variable d'environnement
ENV PYTHONUNBUFFERED=1

# Port expose (si vous avez une API)
EXPOSE 8000

# Commande par defaut
CMD ["python", "-m", "src.models.train"]