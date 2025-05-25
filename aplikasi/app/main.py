from fastapi import FastAPI
from pydantic import BaseModel
from app.predictor import StuntingPredictor, WastingPredictor
from app.rekomendasi import get_articles_by_prediction

app = FastAPI()

@app.get("/")
def root():
    return {"message": "API Stunting Predictor dan Recommendation berjalan."}

# Load model dan scaler
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

API_KEY = "AIzaSyDGOfOgg16rrPdvkaE5Z_L6edLafeEXcIQ"  # Ganti jika diperlukan
SEARCH_ENGINE_ID = "b00ebfb1f84a94c1e"

@app.post("/predict/stunting")
def predict_stunting(input_data: InputData):
    prediction = stunting_model.predict(input_data.data)
    return {"result": prediction}

@app.post("/predict/wasting")
def predict_wasting(input_data: InputData):
    prediction = wasting_model.predict(input_data.data)
    return {"result": prediction}

@app.post("/recommendation")
def recommendation(input_data: CategoryInput):
    try:
        articles = get_articles_by_prediction(API_KEY, SEARCH_ENGINE_ID, input_data.category)
        return {"articles":articles}
    except Exception as e:
        return{"error":str(e)}
