import requests

base_url = "http://127.0.0.1:8000"

input_data = [1, 24, 9.5, 80]

# Prediksi Stunting
response_stunting = requests.post(
    f"{base_url}/predict",
    json={"type": "stunting", "data": input_data}
)
print("Prediksi Stunting:", response_stunting.json())

# Prediksi Wasting
response_wasting = requests.post(
    f"{base_url}/predict",
    json={"type": "wasting", "data": input_data}
)
print("Prediksi Wasting:", response_wasting.json())

# Rekomendasi artikel berdasarkan prediksi Stunting_Sangat Stunting
category = "Stunting_Sangat Stunting"
response_articles = requests.post(
    f"{base_url}/recommendation",
    json={"category": category}
)
print("Status code:", response_articles.status_code)
print("Response text:", response_articles.text)

try:
    print("Artikel Rekomendasi:", response_articles.json())
except Exception as e:
    print("Gagal parsing JSON:", e)