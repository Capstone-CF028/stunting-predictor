from fastapi import FastAPI, UploadFile, Depends
from utils import predictor
from app import inference
from tensorflow.keras.models import load_model
app = FastAPI ()

# Define a global variable to store the model
model = None

def initialize_model():
    global model
    if model is None:
        model = load_model('models/model_wasting.keras')
        return model

