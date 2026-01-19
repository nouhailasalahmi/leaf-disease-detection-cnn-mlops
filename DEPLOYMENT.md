# 🚀 Deployment Guide

Guide complet pour déployer l'application Leaf Disease Detection.

## 📋 Table des matières

1. [Déploiement Local](#local)
2. [Déploiement Docker](#docker)
3. [Déploiement Kubernetes](#kubernetes)
4. [Déploiement Cloud](#cloud)
5. [Configuration Production](#production)

---

## 🏠 Déploiement Local

### Prérequis

- Python 3.9+
- pip
- Git
- 4GB RAM minimum

### Étapes

```bash
# 1. Cloner le projet
git clone https://github.com/nouhailasalahmi/leaf-disease-detection-cnn-mlops.git
cd leaf-disease-detection-cnn-mlops
git lfs pull

# 2. Créer environnement virtuel
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate      # Windows

# 3. Installer dépendances
pip install -r requirements.txt

# 4. Configuration
cp .env.example .env
# Éditer .env selon vos besoins

# 5. Initialiser données (optionnel)
python -c "from src.data.dataset import load_config; load_config()"

# 6. Démarrer MLflow UI
mlflow ui --host 0.0.0.0 --port 5000 &

# 7. Démarrer l'API
python deployment/main.py
```

API disponible à: **http://localhost:8000**

---

## 🐳 Déploiement Docker

### Prérequis

- Docker 20.10+
- Docker Compose 2.0+
- 8GB RAM minimum

### Déploiement Simple (Single Container)

```bash
# 1. Build l'image
docker build -t leaf-disease:latest .

# 2. Run le conteneur
docker run -d \
  --name leaf-disease \
  -p 8000:8000 \
  -e DEBUG=False \
  -e DATABASE_URL="postgresql://user:pass@localhost/db" \
  leaf-disease:latest

# 3. Vérifier les logs
docker logs -f leaf-disease

# 4. Tester l'API
curl http://localhost:8000/health
```

### Déploiement Complet (Docker Compose)

```bash
# 1. Démarrer la stack complète
docker-compose up -d

# 2. Services disponibles
# - API: http://localhost:8000
# - MLflow: http://localhost:5000
# - Prometheus: http://localhost:9090
# - Grafana: http://localhost:3000 (admin/admin)

# 3. Voir les logs
docker-compose logs -f

# 4. Arrêter la stack
docker-compose down
```

### Configuration Docker Compose

Fichier: `deployment/docker-compose.yml`

Services:
- **app**: Application FastAPI principale
- **postgres**: Base de données PostgreSQL
- **mlflow**: MLflow tracking server
- **prometheus**: Monitoring
- **grafana**: Dashboard

---

## ☸️ Déploiement Kubernetes

### Prérequis

- kubectl 1.20+
- Kubernetes 1.20+
- Helm 3.0+ (optionnel)

### Étapes

#### 1. Créer les manifests Kubernetes

```yaml
# k8s/deployment.yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: leaf-disease
spec:
  replicas: 3
  selector:
    matchLabels:
      app: leaf-disease
  template:
    metadata:
      labels:
        app: leaf-disease
    spec:
      containers:
      - name: api
        image: ghcr.io/nouhailasalahmi/leaf-disease:latest
        ports:
        - containerPort: 8000
        env:
        - name: DEBUG
          value: "False"
        - name: DATABASE_URL
          valueFrom:
            secretKeyRef:
              name: app-secrets
              key: database-url
        resources:
          requests:
            memory: "2Gi"
            cpu: "500m"
          limits:
            memory: "4Gi"
            cpu: "2000m"
        livenessProbe:
          httpGet:
            path: /health
            port: 8000
          initialDelaySeconds: 30
          periodSeconds: 10
        readinessProbe:
          httpGet:
            path: /health
            port: 8000
          initialDelaySeconds: 10
          periodSeconds: 5
```

#### 2. Créer les secrets

```bash
# Créer secrets Kubernetes
kubectl create namespace leaf-disease
kubectl create secret generic app-secrets \
  --from-literal=database-url="postgresql://..." \
  -n leaf-disease
```

#### 3. Déployer

```bash
# Appliquer les manifests
kubectl apply -f k8s/ -n leaf-disease

# Vérifier le déploiement
kubectl get deployments -n leaf-disease
kubectl get pods -n leaf-disease

# Port-forward pour tester
kubectl port-forward svc/leaf-disease-api 8000:8000 -n leaf-disease
```

#### 4. Monitoring

```bash
# Logs
kubectl logs -f deployment/leaf-disease -n leaf-disease

# Événements
kubectl get events -n leaf-disease

# Métriques
kubectl top pods -n leaf-disease
```

---

## ☁️ Déploiement Cloud

### AWS (Elastic Container Service)

```bash
# 1. Créer ECR repository
aws ecr create-repository --repository-name leaf-disease

# 2. Build et push
docker build -t leaf-disease:latest .
docker tag leaf-disease:latest \
  YOUR_ACCOUNT_ID.dkr.ecr.YOUR_REGION.amazonaws.com/leaf-disease:latest
aws ecr get-login-password | docker login --username AWS \
  --password-stdin YOUR_ACCOUNT_ID.dkr.ecr.YOUR_REGION.amazonaws.com
docker push YOUR_ACCOUNT_ID.dkr.ecr.YOUR_REGION.amazonaws.com/leaf-disease:latest

# 3. Créer ECS task definition et service
# (Voir documentation AWS ECS)

# 4. Déployer via CloudFormation/Terraform
```

### Google Cloud (Cloud Run)

```bash
# 1. Build avec Cloud Build
gcloud builds submit --tag gcr.io/PROJECT_ID/leaf-disease

# 2. Déployer sur Cloud Run
gcloud run deploy leaf-disease \
  --image gcr.io/PROJECT_ID/leaf-disease \
  --platform managed \
  --region us-central1 \
  --memory 2Gi \
  --set-env-vars DEBUG=False

# 3. Accéder à l'application
gcloud run services describe leaf-disease --platform managed --region us-central1
```

### Azure Container Instances

```bash
# 1. Push vers Azure Container Registry
az acr build --registry MYREGISTRY --image leaf-disease .

# 2. Déployer
az container create \
  --resource-group mygroup \
  --name leaf-disease \
  --image MYREGISTRY.azurecr.io/leaf-disease \
  --cpu 2 --memory 4 \
  --registry-login-server MYREGISTRY.azurecr.io
```

---

## 🔧 Configuration Production

### Variables d'Environnement Essentielles

```bash
# Sécurité
DEBUG=False
SECRET_KEY=your-strong-secret-key-here
ALLOWED_HOSTS=yourdomain.com,api.yourdomain.com

# Base de données (PostgreSQL recommandé)
DATABASE_URL=postgresql://user:password@db.example.com:5432/leaf_disease

# MLflow
MLFLOW_TRACKING_URI=http://mlflow.example.com:5000
MLFLOW_ARTIFACT_ROOT=s3://bucket-name/mlruns

# API
WORKERS=8
CORS_ORIGINS=https://yourdomain.com

# Monitoring
LOG_LEVEL=INFO
PROMETHEUS_ENABLED=True

# Ressources
USE_GPU=True  # Si disponible
NUM_WORKERS=4
```

### Checklist de Sécurité

- [ ] Modifier `SECRET_KEY` et `ALLOWED_HOSTS`
- [ ] Utiliser HTTPS/TLS
- [ ] Configurer PostgreSQL avec mot de passe fort
- [ ] Mettre en place les backups (bases, modèles)
- [ ] Configurer les logs centralisés (ELK Stack, etc.)
- [ ] Mettre en place CORS restrictif
- [ ] Ajouter authentification API (JWT/API Key)
- [ ] Configurer rate limiting
- [ ] Mettre en place monitoring et alertes
- [ ] Tester les failover/recovery

### Performance Tuning

```bash
# Gunicorn workers
WORKERS=$(( 2 * $(nproc) + 1 ))

# Database connection pool
DATABASE_POOL_SIZE=20
DATABASE_MAX_OVERFLOW=40

# Cache
CACHE_BACKEND=redis://redis.example.com:6379

# Compression
GZIP_COMPRESSION=True
```

### Monitoring et Logs

```bash
# Prometheus scrape config
scrape_configs:
  - job_name: 'leaf-disease'
    static_configs:
      - targets: ['localhost:8001']

# Centralised logging (ELK example)
# Filebeat -> Elasticsearch -> Kibana

# Application health checks
GET /health
GET /metrics
```

---

## 📊 Upgrade et Rollback

### Upgrade

```bash
# 1. Récupérer la dernière version
git pull origin main
git lfs pull

# 2. Tests
pytest tests/

# 3. Build nouvelle image
docker build -t leaf-disease:new .

# 4. Tester la nouvelle image
docker run --rm leaf-disease:new pytest

# 5. Déployer
docker tag leaf-disease:new leaf-disease:latest
docker-compose up -d

# 6. Vérifier
curl http://localhost:8000/health
```

### Rollback

```bash
# Revenir à la version précédente
docker-compose down
docker run -d \
  --name leaf-disease \
  leaf-disease:previous-version
```

---

## 🆘 Troubleshooting

### L'API ne démarre pas

```bash
# Vérifier les logs
docker logs leaf-disease

# Vérifier les ressources
docker stats leaf-disease

# Redémarrer
docker restart leaf-disease
```

### Problèmes de modèle

```bash
# Vérifier le modèle
python -c "import tensorflow as tf; m = tf.keras.models.load_model('models/plant_disease_model.h5'); print(m.summary())"

# Télécharger via Git LFS
git lfs pull --include="*.h5"
```

### Base de données

```bash
# Vérifier la connexion
python -c "import sqlalchemy; print(sqlalchemy.create_engine(DATABASE_URL).connect())"

# Réinitialiser
# WARNING: Ceci supprime toutes les données
python -c "from src.database import Base, engine; Base.metadata.drop_all(engine); Base.metadata.create_all(engine)"
```

---

## 📞 Support

- Documentation: [README.md](../README.md)
- Issues: GitHub Issues
- Email: nouhail.salahmi@example.com

---

**Dernière mise à jour:** Janvier 2026
