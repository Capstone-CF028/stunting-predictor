import tensorflow as tf
import numpy as np

# Load model hanya sekali
stunting_model = tf.keras.models.load_model('models/model_stunting.h5')
wasting_model = tf.keras.models.load_model('models/model_wasting.keras')

def predict_stunting(data_input):
    input_array = np.array([data_input])  # Data harus dalam bentuk array 2D
    prediction = stunting_model.predict(input_array)
    label = np.argmax(prediction)
    return label

def predict_wasting(data_input):
    input_array = np.array([data_input])
    prediction = wasting_model.predict(input_array)
    label = np.argmax(prediction)
    return label
