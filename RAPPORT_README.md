# 📄 Guide pour le Rapport LaTeX

Ce dossier contient le rapport complet du projet de classification des maladies des feuilles en LaTeX.

## 📋 Contenu du Rapport

Le rapport `rapport.tex` contient :

- ✅ **Page de titre** - Couverture professionnelle
- ✅ **Résumé/Abstract** - Synthèse du projet
- ✅ **Table des matières** - Navigation complète
- ✅ **Chapitre 1** : Introduction et contexte
- ✅ **Chapitre 2** : Architecture et méthodologie
- ✅ **Chapitre 3** : Implémentation et code
- ✅ **Chapitre 4** : Résultats et évaluation
- ✅ **Chapitre 5** : Déploiement et MLOps
- ✅ **Chapitre 6** : Conclusion et perspectives
- ✅ **Bibliographie** - Références scientifiques
- ✅ **Appendices** - Détails supplémentaires

## 🛠️ Prérequis

Pour compiler le rapport LaTeX, vous avez besoin de :

### Option 1: Installation Locale

**Windows:**
```bash
# Installer MiKTeX depuis https://miktex.org/download
# Ou installer TexLive depuis https://tug.org/texlive/
```

**macOS:**
```bash
brew install mactex
# ou
brew install basictex
```

**Linux (Ubuntu/Debian):**
```bash
sudo apt-get install texlive-latex-full texlive-fonts-recommended texlive-latex-extra texlive-lang-french
```

### Option 2: Compilateur en Ligne

- **Overleaf** : https://www.overleaf.com/ (Gratuit)
- **Papeeria** : https://papeeria.com/
- **CoCalc** : https://cocalc.com/

## 📝 Compilation

### Méthode 1: Ligne de Commande

```bash
# Compilation simple
pdflatex rapport.tex

# Compilation avec références (recommandé)
pdflatex rapport.tex
bibtex rapport
pdflatex rapport.tex
pdflatex rapport.tex

# Nettoyer les fichiers temporaires
rm -f rapport.aux rapport.bbl rapport.blg rapport.log rapport.out rapport.toc
```

### Méthode 2: Avec Script

```bash
# Créer le fichier compile.sh
#!/bin/bash
pdflatex -interaction=nonstopmode rapport.tex
bibtex rapport
pdflatex -interaction=nonstopmode rapport.tex
pdflatex -interaction=nonstopmode rapport.tex
rm -f rapport.aux rapport.bbl rapport.blg rapport.log rapport.out

# Rendre exécutable et lancer
chmod +x compile.sh
./compile.sh
```

### Méthode 3: Avec Makefile

```bash
# Créer Makefile
make
# ou
make clean
```

## 📤 Upload sur Overleaf

1. Allez sur https://www.overleaf.com/
2. Cliquez sur "New Project" → "Upload Project"
3. Téléchargez le fichier `rapport.tex`
4. Cliquez sur "Recompile" pour voir le PDF

## 🎨 Personnalisation

Pour personnaliser le rapport :

### Modifier le Titre
```latex
\title{
    \textbf{\Large Rapport de Projet} \\[0.5cm]
    \textbf{\huge VOTRE TITRE ICI} \\
    ...
}
```

### Modifier l'Auteur
```latex
\author{
    VOTRE NOM \\[0.3cm]
    \textit{VOTRE TITRE}
}
```

### Modifier les Couleurs
```latex
\usepackage{xcolor}

% Ajouter après la déclaration
\definecolor{maCouleur}{rgb}{0.2, 0.4, 0.6}

% Utiliser
\textcolor{maCouleur}{Texte coloré}
```

### Modifier la Géométrie (Marges)
```latex
\geometry{left=2.0cm, right=2.0cm, top=2.0cm, bottom=2.0cm}
```

### Ajouter des Images

```latex
\begin{figure}[H]
\centering
\includegraphics[width=0.7\textwidth]{path/to/image.png}
\caption{Description de l'image}
\label{fig:mon_image}
\end{figure}

% Référencer
Voir la figure \ref{fig:mon_image}
```

## 📚 Sections Principales

### Ajouter un Chapitre
```latex
\chapter{Mon Nouveau Chapitre}

\section{Ma Section}

\subsection{Ma Sous-section}

Contenu ici...
```

### Ajouter une Table
```latex
\begin{table}[H]
\centering
\caption{Ma Table}
\begin{tabular}{|c|c|c|}
\hline
En-tête 1 & En-tête 2 & En-tête 3 \\
\hline
Donnée 1 & Donnée 2 & Donnée 3 \\
\hline
\end{tabular}
\end{table}
```

### Ajouter du Code
```latex
\begin{lstlisting}[language=Python, caption=Mon Code]
def ma_fonction():
    return 42
\end{lstlisting}
```

### Ajouter une Équation
```latex
% Inline
L'équation suivante : $E = mc^2$

% Display
\begin{equation}
E = mc^2
\end{equation}
```

## 🐛 Troubleshooting

### Erreur: "File not found"
```bash
# Assurez-vous que tous les fichiers sont dans le bon répertoire
# Vérifiez les chemins d'images et d'imports
```

### Erreur: "Undefined reference"
```latex
% Compilez plusieurs fois
pdflatex rapport.tex  # 1ère fois
bibtex rapport        # Traiter les références
pdflatex rapport.tex  # 2ème fois
pdflatex rapport.tex  # 3ème fois (finaliser)
```

### La table des matières est vide
```latex
% Compilez au moins 2 fois pour générer la table des matières
pdflatex rapport.tex
pdflatex rapport.tex
```

### Problèmes d'encodage UTF-8
```latex
% Assurez-vous que ce package est au début :
\usepackage[utf-8]{inputenc}
\usepackage[french]{babel}
```

## 📖 Ressources Utiles

- **Overleaf Tutorials**: https://www.overleaf.com/learn
- **LaTeX Stack Exchange**: https://tex.stackexchange.com/
- **Documentation MiKTeX**: https://miktex.org/help
- **Documentation TeX Live**: https://tug.org/texlive/
- **LaTeX Wikibook**: https://en.wikibooks.org/wiki/LaTeX

## 📊 Export et Partage

### Exporter en PDF
```bash
# PDF généré automatiquement
# Fichier: rapport.pdf
```

### Exporter en HTML (optionnel)
```bash
# Installer pandoc
pip install pandoc

# Convertir
pandoc rapport.tex -t html -o rapport.html
```

### Exporter en DOCX (optionnel)
```bash
# Convertir vers Word
pandoc rapport.tex -t docx -o rapport.docx
```

## 💡 Conseils

1. **Backup régulier** : Sauvegardez votre work.tex
2. **Version control** : Utilisez Git pour tracker les changements
3. **Structure claire** : Organisez en dossiers/fichiers séparés pour de gros rapports
4. **Références croisées** : Utilisez `\ref{}` et `\label{}`
5. **Commentaires** : Documentez votre LaTeX avec `%`

## 📧 Support

Pour des questions sur le rapport ou LaTeX :
- Consultez le README.md principal
- Ouvrez une issue sur GitHub
- Email: nouhail.salahmi@example.com

---

**Dernière mise à jour:** Janvier 2026
