
'''from fastapi import FastAPI, UploadFile, Depends
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

'''
from predictor import StuntingPredictor, WastingPredictor

stunting_pred = StuntingPredictor('models/model_stunting.h5', 'stunting-predictior-ml/scaler.pkl')
wasting_pred = WastingPredictor('models/model_wasting.keras', 'stunting-predictior-ml/scaler_wt.pkl')

input_stunting = [0, 10, 70, 8]
input_wasting = [0, 10, 70, 8]

hasil_stunting = stunting_pred.predict(input_stunting)
hasil_wasting = wasting_pred.predict(input_wasting)

print("Hasil prediksi stunting:", hasil_stunting)
print("Hasil prediksi wasting:", hasil_wasting)