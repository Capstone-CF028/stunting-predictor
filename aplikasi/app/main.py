from fastapi import FastAPI
from pydantic import BaseModel
from app.predictor import StuntingPredictor, WastingPredictor

app = FastAPI()

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
    data: list  # Contoh: [jenis_kelamin, usia, berat, tinggi]

@app.post("/predict/stunting")
def predict_stunting(input_data: InputData):
    prediction = stunting_model.predict(input_data.data)
    return {"result": prediction}

@app.post("/predict/wasting")
def predict_wasting(input_data: InputData):
    prediction = wasting_model.predict(input_data.data)
    return {"result": prediction}
