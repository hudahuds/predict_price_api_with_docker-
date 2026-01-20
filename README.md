#🏠 House Price Prediction API (FastAPI + Docker)

##Ce projet est une API de prédiction de prix immobilier construite avec FastAPI, un modèle de Machine Learning (XGBoost) et Docker pour la conteneurisation.

L’objectif est de fournir une API simple, rapide et prête au déploiement permettant de prédire le prix d’une maison à partir de caractéristiques numériques.


##🚀 Technologies utilisées

Python 3.12

FastAPI – Framework API rapide et moderne

Uvicorn – Serveur ASGI

XGBoost – Modèle de Machine Learning

Docker & Docker Compose – Conteneurisation

Pydantic – Validation des données

##📌 Endpoints disponibles
Vérification de l’API

GET /
{ end points disponibles
Vérification de l’API   }

Prédiction de prix

Exemple de requête :

{
"feature1": 120,
"feature2": 3,
"feature3": 1
}

Exemple de réponse :

{
"predicted_price": 245000.75
}



