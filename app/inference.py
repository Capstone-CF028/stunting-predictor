import numpy as np
import os
from tensorflow.keras.models import load_model
from sklearn.metrics import classification_report, accuracy_score

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

X_test_path = os.path.join(BASE_DIR, '..', 'stunting-predictor-ml', 'data', 'data_uji', 'X_test_st.npy')
y_test_path = os.path.join(BASE_DIR, '..', 'stunting-predictor-ml', 'data', 'data_uji', 'y_test_st.npy')
model_path = os.path.join(BASE_DIR, '..', 'stunting-predictor-ml', 'Model_Stunting', 'model_stunting.h5')

X_test_st = np.load(X_test_path)
y_test_st = np.load(y_test_path)

model = load_model(model_path)

y_pred_probs = model.predict(X_test_st)

y_pred = np.argmax(y_pred_probs, axis=1)

y_true = np.argmax(y_test_st, axis=1)

class_names = ['Normal', 'Sangat Stunting', 'Stunting']

print(classification_report(y_true, y_pred, target_names=class_names))

accuracy = accuracy_score(y_true, y_pred)
print(f"Akurasi: {accuracy:.4f}")

print("Hasil prediksi (kelas):")
print(y_pred)

