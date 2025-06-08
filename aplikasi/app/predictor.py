import numpy as np
import joblib
import pandas as pd
from tensorflow.keras.models import load_model

class StuntingPredictor:
    def __init__(self, model_path, scaler_path):
        self.model = load_model(model_path)
        self.scaler = joblib.load(scaler_path)
        self.labels = ['Normal', 'Sangat Stunting', 'Stunting', 'Tinggi']  

    def preprocess(self, input_data):
        arr = np.array(input_data, dtype=float)
        if arr.ndim == 1:
            arr = arr.reshape(1, -1)
        df = pd.DataFrame(arr, columns=[
            'Jenis Kelamin', 
            'Umur (bulan)', 
            'Tinggi Badan (cm)', 
            'Berat Badan (kg)'
        ])
        arr_scaled = self.scaler.transform(df)
        return arr_scaled

    def predict(self, input_data):
        try:
            print("👉 input_data:", input_data)

            x = self.preprocess(input_data)
            print("✅ after preprocess, shape:", x.shape)

            pred_probs = self.model.predict(x)
            print("✅ model.predict output shape:", pred_probs.shape)
            print("✅ model.predict output:", pred_probs)

            if pred_probs.shape[0] == 0:
                raise ValueError("Model tidak menghasilkan prediksi.")

            pred_index = np.argmax(pred_probs, axis=1)[0]
            print("✅ pred_index:", pred_index)

            pred_label = self.labels[pred_index]
            print("✅ pred_label:", pred_label)

            return pred_label
        except Exception as e:
            print("❌ Error saat prediksi Stunting:", e)
            raise

class WastingPredictor:
    def __init__(self, model_path, scaler_path):
        self.model = load_model(model_path)
        self.scaler = joblib.load(scaler_path)
        self.labels = ['Normal', 'Risiko Kegemukan', 'Sangat Kurus', 'Kurus']  # Sesuaikan label

    def preprocess(self, input_data):
        arr = np.array(input_data, dtype=float)
        if arr.ndim == 1:
            arr = arr.reshape(1, -1)
        df = pd.DataFrame(arr, columns=[
            'Jenis Kelamin', 
            'Umur (bulan)', 
            'Tinggi Badan (cm)', 
            'Berat Badan (kg)'
        ])
        arr_scaled = self.scaler.transform(df)
        return arr_scaled

    def predict(self, input_data):
        try:
            x = self.preprocess(input_data)
            pred_probs = self.model.predict(x)

            if pred_probs.shape[0] == 0:
                raise ValueError("Model tidak menghasilkan prediksi.")

            pred_index = np.argmax(pred_probs, axis=1)[0]
            pred_label = self.labels[pred_index]
            return pred_label
        except Exception as e:
            print("❌ Error saat prediksi Wasting:", e)
            raise
