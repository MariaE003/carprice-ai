# carprice-ai
# Prédicteur de Prix de Voitures d'Occasion

## Description

Ce projet consiste à développer un modèle de Machine Learning
capable d'estimer le prix de vente d'une voiture d'occasion.

## Données

Les variables utilisées sont :

- Year
- Km_Driven
- Fuel
- Seller_Type
- Transmission
- Owner

La variable cible est :

- Selling_Price

## Étapes du projet

### 1. Exploration et nettoyage

- Analyse des données
- Traitement des valeurs manquantes
- Suppression des doublons
- Détection des valeurs aberrantes
- Encodage des variables catégoriques

### 2. Entraînement

Les modèles suivants ont été testés :

- Linear Regression
- Random Forest
- XGBoost
- SVR

### 3. Optimisation

Les modèles Random Forest et XGBoost ont été optimisés
avec GridSearchCV et une validation croisée à 5 folds.

### 4. Comparaison

Les modèles sont comparés avec :

- MAE
- RMSE
- R²

Des graphiques de résidus et de prédictions sont également utilisés.

### 5. Application

Le modèle final est sauvegardé avec Joblib et utilisé
dans une interface Streamlit.

## Installation

```bash
pip install -r requirements.txt