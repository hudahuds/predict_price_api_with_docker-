# Image Python slim
FROM python:3.11

# Définir le dossier de travail
WORKDIR /app

# Copier le code app et les modèles dans le conteneur 
COPY app /app
# Installer les dépendances Python
RUN pip install --upgrade pip && \
    pip install --no-cache-dir --default-timeout=7000 \
    fastapi \
    uvicorn \
    xgboost==2.1.2 \
    pandas \
    scikit-learn

# Exposer le port
EXPOSE 8000

# Commande pour lancer l'API
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
