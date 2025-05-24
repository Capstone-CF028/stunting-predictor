import requests

def call_google_search_api(api_key, search_engine_id, query):
    url = f"https://www.googleapis.com/customsearch/v1"
    params = {
        "key": api_key,
        "cx": search_engine_id,
        "q": query,
        "num": 5  # jumlah hasil artikel yang diambil, maksimal 10
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        print("Error:", response.status_code, response.text)
        return None

def get_articles_by_prediction(api_key, search_engine_id, prediction_category):
    if prediction_category == "stunting_berat":
        query = "stunting berat gejala pencegahan"
    elif prediction_category == "stunting_ringan":
        query = "stunting ringan nutrisi pencegahan"
    elif prediction_category == "normal":
        query = "tumbuh kembang sehat nutrisi anak"
    else:
        query = "stunting pencegahan"

    data = call_google_search_api(api_key, search_engine_id, query)
    if data and "items" in data:
        articles = []
        for item in data["items"]:
            title = item.get("title")
            link = item.get("link")
            articles.append({"title": title, "link": link})
        return articles
    else:
        return []

# contoh pemakaian:
if __name__ == "__main__":
    # kode utama kamu di sini

    API_KEY = "AIzaSyDGOfOgg16rrPdvkaE5Z_L6edLafeEXcIQ"
    SEARCH_ENGINE_ID = "b00ebfb1f84a94c1e"

    kategori_prediksi = "stunting_berat"  # contoh input dari hasil prediksi model

    hasil_artikel = get_articles_by_prediction(API_KEY, SEARCH_ENGINE_ID, kategori_prediksi)

    print("Artikel rekomendasi berdasarkan prediksi:", kategori_prediksi)
    for artikel in hasil_artikel:
        print("-", artikel["title"])
        print("  Link:", artikel["link"])