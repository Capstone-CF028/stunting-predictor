import requests

def call_google_search_api(api_key, search_engine_id, query):
    url = "https://www.googleapis.com/customsearch/v1"
    params = {
        "key": api_key,
        "cx": search_engine_id,
        "q": query,
        "num": 10
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        print("Error:", response.status_code, response.text)
        return None

def get_articles_by_prediction(api_key, search_engine_id, prediction_category):
    allowed_sites = (
        "site:detik.com OR site:kompas.com OR site:halodoc.com OR site:alodokter.com OR "
        "site:unicef OR site:kemkes.go.id OR site:who.int OR site:hellosehat.com OR "
        "site:siloamhospitals.com"
    )

    if prediction_category == "Stunting_Sangat Stunting":
        query = "stunting berat gejala pencegahan " + allowed_sites
    elif prediction_category == "Stunting_Stunting":
        query = "stunting ringan nutrisi pencegahan " + allowed_sites
    elif prediction_category == "Stunting_Normal":
        query = "tumbuh kembang sehat nutrisi anak " + allowed_sites
    elif prediction_category == "Wasting_Normal":
        query = "status gizi anak normal tips kesehatan " + allowed_sites
    elif prediction_category == "Wasting_Resiko Kegemukan":
        query = "anak risiko kegemukan pola makan sehat " + allowed_sites
    elif prediction_category == "Wasting_Sangat Kurus":
        query = "wasting sangat kurus balita penyebab dan pencegahan " + allowed_sites
    elif prediction_category == "Wasting_Kurus":
        query = "wasting kurus pada anak penyebab solusi " + allowed_sites
    else:
        query = "masalah gizi pada anak dan pencegahannya " + allowed_sites

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