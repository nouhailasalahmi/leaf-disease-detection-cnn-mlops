# 🤝 Contribution Guide

Merci d'être intéressé par la contribution à ce projet ! Voici comment vous pouvez aider.

## Code of Conduct

Nous adhérons à une culture d'inclusion et de respect. Tous les contributeurs doivent se comporter avec respect et bienveillance.

## Comment contribuer

### 1️⃣ Signaler un Bug

Avez-vous trouvé un bug ? Veuillez créer une issue GitHub avec:

- **Titre clair et descriptif**
- **Description détaillée** du problème
- **Étapes de reproduction** (précises)
- **Comportement attendu** vs **comportement observé**
- **Screenshots/logs** (si applicable)
- **Environnement** (OS, Python version, etc.)

### 2️⃣ Suggérer une Amélioration

Les suggestions sont bienvenues ! Créez une issue avec le tag `enhancement`:

- Décrivez clairement la fonctionnalité souhaitée
- Expliquez pourquoi ce serait utile
- Listez les exemples d'utilisation possibles

### 3️⃣ Soumettre une Pull Request

#### Étape 1: Fork le repository

```bash
# Visitez https://github.com/nouhailasalahmi/leaf-disease-detection-cnn-mlops
# Cliquez sur "Fork"
```

#### Étape 2: Clone votre fork

```bash
git clone https://github.com/YOUR_USERNAME/leaf-disease-detection-cnn-mlops.git
cd leaf-disease-detection-cnn-mlops
git remote add upstream https://github.com/nouhailasalahmi/leaf-disease-detection-cnn-mlops.git
```

#### Étape 3: Créez une branche feature

```bash
git checkout -b feature/ma-super-feature
# ou pour un bug
git checkout -b fix/description-du-bug
```

#### Étape 4: Développez votre changement

```bash
# Installez les dépendances de développement
pip install -r requirements.txt
pip install pytest black flake8 isort

# Faites vos modifications...

# Testez votre code
pytest tests/

# Formatez votre code
black src/ tests/
isort src/ tests/
flake8 src/ tests/
```

#### Étape 5: Committez vos changements

Utilisez des messages de commit clairs et descriptifs:

```bash
git commit -m "feat: Ajoute support pour modèles TensorFlow Lite"
# ou
git commit -m "fix: Corrige le bug de décodage d'image PNG"
# ou
git commit -m "docs: Améliore la documentation de l'API"
```

**Préfixes de commit recommandés:**
- `feat:` - Nouvelle fonctionnalité
- `fix:` - Correction de bug
- `docs:` - Changements de documentation
- `style:` - Formatage, pas de changement logique
- `refactor:` - Refactorisation du code
- `perf:` - Amélioration de performance
- `test:` - Ajout ou modification de tests
- `ci:` - Changements CI/CD

#### Étape 6: Synchronisez avec la branche upstream

```bash
git fetch upstream
git rebase upstream/main
```

#### Étape 7: Poussez vers votre fork

```bash
git push origin feature/ma-super-feature
```

#### Étape 8: Ouvrez une Pull Request

- Allez sur https://github.com/YOUR_USERNAME/leaf-disease-detection-cnn-mlops
- Cliquez sur "Compare & pull request"
- Remplissez le template PR
- Assurez-vous que tous les checks passent

## Guidelines de Développement

### Style de Code

Nous suivons [PEP 8](https://pep8.org/). Utilisez les outils:

```bash
# Format automatique
black src/ tests/

# Vérifier la conformité
flake8 src/ tests/ --max-line-length=100

# Organiser les imports
isort src/ tests/
```

### Tests

Tous les nouveaux codes doivent avoir des tests:

```bash
# Écrire des tests
# Exemples dans: tests/test_*.py

# Exécuter les tests
pytest tests/ -v

# Avec couverture
pytest tests/ --cov=src --cov-report=html
```

### Documentation

- Documentez toutes les fonctions publiques avec docstrings
- Mettez à jour le README si vous changez le comportement
- Commentez le code complexe
- Mettez à jour CHANGELOG.md

### Commits

- **Atomiques:** Un changement logique par commit
- **Descriptifs:** Messages clairs et détaillés
- **Squash:** Combinez les commits logiquement liés

```bash
# Avant de faire un PR, squash les commits si nécessaire
git rebase -i HEAD~3  # Rebase derniers 3 commits
```

## Process de Review

1. **Automated Checks:**
   - GitHub Actions CI/CD
   - Code linting
   - Tests coverage

2. **Code Review:**
   - Au moins 1 reviewer
   - Discussions constructives
   - Suggestions d'amélioration

3. **Merge:**
   - Tous les checks doivent passer
   - Au moins 1 approbation
   - Branche à jour avec main

## Conventions du Projet

### Structure des Fichiers

```
src/
├── models/        # Logique de modèles
├── data/          # Gestion des données
└── utils/         # Utilitaires
```

### Nommage

- **Fonctions/Variables:** `snake_case`
- **Classes:** `PascalCase`
- **Constantes:** `UPPER_SNAKE_CASE`
- **Fichiers privés:** `_private_function`

### Type Hints

Ajoutez des type hints autant que possible:

```python
def predict(image: np.ndarray) -> Dict[str, float]:
    """Fait une prédiction sur une image."""
    pass
```

## Questions ?

- 💬 Discussions GitHub: https://github.com/nouhailasalahmi/leaf-disease-detection-cnn-mlops/discussions
- 📧 Email: nouhail.salahmi@example.com
- 📚 Wiki: [Voir la wiki du projet]

## Merci! 🎉

Vos contributions rendent ce projet meilleur pour tout le monde.

---

**En soumettant une PR, vous acceptez que vos contributions soient sous licence MIT.**
