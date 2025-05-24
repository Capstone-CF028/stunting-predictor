import numpy as np
import joblib
from tensorflow.keras.models import load_model

class StuntingPredictor:
    def _init_(self, model_path, scaler_path):
        self.model = load_model(model_path)
        self.scaler = joblib.load(scaler_path)

    def preprocess(self, input_data):
        arr = np.array(input_data, dtype=float).reshape(1, -1)
        arr_scaled = self.scaler.transform(arr)
        return arr_scaled

    def predict(self, input_data):
        x = self.preprocess(input_data)
        pred = self.model.predict(x)
        return pred


class WastingPredictor:
    def _init_(self, model_path, scaler_path):
        self.model = load_model(model_path)
        self.scaler = joblib.load(scaler_path)

    def preprocess(self, input_data):
        arr = np.array(input_data, dtype=float).reshape(1, -1)
        arr_scaled = self.scaler.transform(arr)
        return arr_scaled

    def predict(self, input_data):
        x = self.preprocess(input_data)
        pred = self.model.predict(x)
        return pred