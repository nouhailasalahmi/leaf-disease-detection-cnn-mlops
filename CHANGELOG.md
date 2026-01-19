# Changelog

Tous les changements notables de ce projet sont documentés ici.

Le format est basé sur [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
et ce projet adhère à [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added
- Nouveau système de logging structuré
- Support pour modèles TensorFlow Lite
- API endpoint pour monitoring en temps réel

### Changed
- Amélioration des performances du modèle CNN
- Refactorisation de la pipeline de données

### Fixed
- Correction du bug de décodage d'images PNG
- Amélioration de la gestion des erreurs

## [1.0.0] - 2026-01-19

### Added
- 🎉 Lancement initial du projet
- Classification de maladies des feuilles (3 classes: Healthy, Powdery, Rust)
- API FastAPI pour prédictions
- Pipeline d'entraînement avec MLflow
- Dashboard Grafana pour monitoring
- Docker et Docker Compose pour déploiement
- GitHub Actions pour CI/CD
- Tests unitaires avec pytest
- Documentation complète

### Features
- ✨ CNN personnalisée avec augmentation de données
- 📊 MLflow tracking pour expériences
- 📈 Métriques Prometheus
- 🐳 Containerisation Docker
- 🔄 CI/CD automatisé
- 🧪 Suite de tests complète
- 📚 Documentation et guides

### Performance
- Précision du modèle: ~96%
- Temps d'inférence: ~200ms/image
- Temps d'entraînement: ~2h (GPU)

---

## Format

### Added
Pour les nouvelles fonctionnalités.

### Changed
Pour les changements dans les fonctionnalités existantes.

### Deprecated
Pour les fonctionnalités bientôt supprimées.

### Removed
Pour les fonctionnalités supprimées.

### Fixed
Pour les corrections de bugs.

### Security
Pour les vulnérabilités de sécurité.

---

## Versioning

Les versions suivent [Semantic Versioning](https://semver.org/):
- **MAJOR**: Changements incompatibles
- **MINOR**: Nouvelles fonctionnalités rétro-compatibles
- **PATCH**: Corrections de bugs rétro-compatibles

Exemples:
- `1.0.0` - Release initiale
- `1.1.0` - Nouvelles fonctionnalités
- `1.1.1` - Correction de bugs
- `2.0.0` - Changements majeurs/incompatibles

---

Pour plus de détails, consultez les [commits](https://github.com/nouhailasalahmi/leaf-disease-detection-cnn-mlops/commits/main).
