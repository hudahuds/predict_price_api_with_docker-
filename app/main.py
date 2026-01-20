from fastapi import FastAPI
from schemas import HouseFeatures
from services.predictor import predict_price

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "API de prédiction de prix de maison"}

@app.post("/predict")
def predict(house: HouseFeatures):
    price = predict_price(house)
    return {"predicted_price": round(price, 2)}
