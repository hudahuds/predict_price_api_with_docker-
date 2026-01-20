from fastapi import FastAPI
from pydantic import BaseModel
import pickle
import numpy as np
import xgboost as xgb
from schemas import HouseFeatures

# Charger le modèle UNE SEULE FOIS au démarrage
MODEL_PATH = "/app/models/xgb_model.pkl"

with open(MODEL_PATH, "rb") as f:
    xgb_model = pickle.load(f)


def predict_price(house: HouseFeatures) -> float:
    """
    Prédit le prix d'une maison à partir des features fournies
    """

    X = np.array([[
        house.bedrooms,
        house.bathrooms,
        house.sqft_living,
        house.sqft_lot,
        house.floors,
        house.waterfront,
        house.view,
        house.condition,
        house.sqft_above,
        house.sqft_basement,
        house.age_of_house,
        house.has_been_renovated
    ]])

    prediction = xgb_model.predict(X)

    return float(prediction[0])