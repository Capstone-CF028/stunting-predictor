import numpy as np
import joblib
from tensorflow.keras.models import load_model

class StuntingPredictor:
    def __init__(self, model_path, scaler_path):
        self.model = load_model(model_path)
        self.scaler = joblib.load(scaler_path)
        self.labels = ['Normal', 'Stunting', 'Sangat Stunting']  # ganti sesuai label modelmu

    def preprocess(self, input_data):
        arr = np.array(input_data, dtype=float).reshape(1, -1)
        arr_scaled = self.scaler.transform(arr)
        return arr_scaled

    def predict(self, input_data):
        x = self.preprocess(input_data)
        pred_probs = self.model.predict(x)
        pred_index = np.argmax(pred_probs)
        pred_label = self.labels[pred_index]
        return pred_label
    
class WastingPredictor:
    def __init__(self, model_path, scaler_path):
        self.model = load_model(model_path)
        self.scaler = joblib.load(scaler_path)
        self.labels = ['Normal', 'Resiko Kegemukan', 'Sangat Kurus', 'Kurus']  # ganti sesuai label modelmu

    def preprocess(self, input_data):
        arr = np.array(input_data, dtype=float).reshape(1, -1)
        arr_scaled = self.scaler.transform(arr)
        return arr_scaled

    def predict(self, input_data):
        x = self.preprocess(input_data)
        pred_probs = self.model.predict(x)
        pred_index = np.argmax(pred_probs)
        pred_label = self.labels[pred_index]
        return pred_label
