from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from app.predictor import StuntingPredictor, WastingPredictor
from app.rekomendasi import get_articles_by_prediction
import logging

app = FastAPI()

origins = [
    "http://localhost:3000",
    "http://127.0.0.1:3000"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

stunting_model = StuntingPredictor(
    model_path="models/model_stunting.h5",
    scaler_path="scaler/scaler.pkl"
)

wasting_model = WastingPredictor(
    model_path="models/model_wasting.keras",
    scaler_path="scaler/scaler_wt.pkl"
)

class InputData(BaseModel):
    data: list

class CategoryInput(BaseModel):
    category: str

API_KEY = "AIzaSyDGOfOgg16rrPdvkaE5Z_L6edLafeEXcIQ"
SEARCH_ENGINE_ID = "b00ebfb1f84a94c1e"

@app.get("/")
def root():
    return {"message": "API Stunting Predictor dan Recommendation berjalan."}

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

@app.post("/recommendation")
def recommendation(input_data: CategoryInput):
    try:
        articles = get_articles_by_prediction(API_KEY, SEARCH_ENGINE_ID, input_data.category)
        return {"articles": articles}
    except Exception as e:
        logger.error(f"Error during recommendation retrieval: {e}")
        raise HTTPException(status_code=500, detail=f"Recommendation error: {str(e)}")

@app.post("/predict-and-recommend")
def predict_and_recommend(input_data: InputData):
    try:
        # Prediksi dari input
        stunting_label = stunting_model.predict(input_data.data)
        wasting_label = wasting_model.predict(input_data.data)

        # Tentukan label kategori
        if "Stunting" in stunting_label:
            category = f"Stunting_{stunting_label}"
        else:
            category = f"Wasting_{wasting_label}"

        # Ambil artikel dari kategori gabungan
        articles = get_articles_by_prediction(API_KEY, SEARCH_ENGINE_ID, category)

        return {
            "stunting": stunting_label,
            "wasting": wasting_label,
            "category_used": category,
            "articles": articles
        }
    except Exception as e:
        return {"error": str(e)}
