from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from app.predictor import StuntingPredictor, WastingPredictor
from app.rekomendasi import get_articles_by_prediction
import logging

app = FastAPI()


origins = [
    "http://localhost:5500",
    "http://127.0.0.1:5500",
    "http://localhost:5173",       
    "http://127.0.0.1:5173"         
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Load model dan scaler
stunting_model = StuntingPredictor(
    model_path="models/model_stunting.h5",
    scaler_path="scaler/scaler.pkl"
)

wasting_model = WastingPredictor(
    model_path="models/model_wasting.keras",
    scaler_path="scaler/scaler_wt.pkl"
)

# Schema untuk input data
class InputData(BaseModel):
    data: list

class CategoryInput(BaseModel):
    category: str

# API Key dan Search Engine ID untuk Google Search
from dotenv import load_dotenv
import os

load_dotenv()  # untuk memuat file .env

API_KEY = os.getenv("API_KEY")
SEARCH_ENGINE_ID = os.getenv("SEARCH_ENGINE_ID")

@app.get("/")
def root():
    return {"message": "API Stunting-Wasting Predictor dan Rekomendasi berjalan."}

@app.post("/predict/stunting")
def predict_stunting(input_data: InputData):
    try:
        logger.info(f"Received stunting prediction request with data: {input_data.data}")
        prediction = stunting_model.predict(input_data.data)
        logger.info(f"Stunting prediction result: {prediction}")
        return {"result": prediction}
    except Exception as e:
        logger.error(f"Error during stunting prediction: {e}")
        raise HTTPException(status_code=500, detail=f"Prediction error: {str(e)}")

@app.post("/predict/wasting")
def predict_wasting(input_data: InputData):
    try:
        logger.info(f"Received wasting prediction request with data: {input_data.data}")
        prediction = wasting_model.predict(input_data.data)
        logger.info(f"Wasting prediction result: {prediction}")
        return {"result": prediction}
    except Exception as e:
        logger.error(f"Error during wasting prediction: {e}")
        raise HTTPException(status_code=500, detail=f"Prediction error: {str(e)}")

@app.post("/predict-and-recommend")
def predict_and_recommend(input_data: InputData):
    try:
        stunting_label = stunting_model.predict(input_data.data)
        wasting_label = wasting_model.predict(input_data.data)

        combined_category = f"Stunting_{stunting_label} + Wasting_{wasting_label}"

        # Tentukan kategori dominan untuk query artikel
        if stunting_label != "Normal":
            category = f"Stunting_{stunting_label}"
        elif wasting_label != "Normal":
            category = f"Wasting_{wasting_label}"
        else:
            category = "Wasting_Normal"

        articles = get_articles_by_prediction(API_KEY, SEARCH_ENGINE_ID, category)

        return {
            "stunting": stunting_label,
            "wasting": wasting_label,
            "combined_category": combined_category,
            "used_for_query": category,
            "articles": articles
        }
    except Exception as e:
        logger.error(f"Error during combined prediction and recommendation: {e}")
        raise HTTPException(status_code=500, detail=f"Prediction error: {str(e)}")