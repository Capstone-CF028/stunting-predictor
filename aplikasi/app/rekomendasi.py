import requests

def call_google_search_api(api_key, search_engine_id, query, exact_terms=None):
    url = "https://www.googleapis.com/customsearch/v1"
    params = {
        "key": api_key,
        "cx": search_engine_id,
        "q": query,
        "num": 5
    }
    if exact_terms:
        params["exactTerms"] = exact_terms

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

    exact_terms = None

    if prediction_category == "Stunting_Sangat Stunting":
        query = "stunting berat pada anak gejala pencegahan dampak " + allowed_sites
        exact_terms = "stunting"
    elif prediction_category == "Stunting_Stunting":
        query = "stunting ringan nutrisi pencegahan cara mengatasi stunting " + allowed_sites
        exact_terms = "stunting"
    elif prediction_category == "Stunting_Normal":
        query = "tips tumbuh kembang sehat nutrisi anak normal stimulasi optimal " + allowed_sites
    elif prediction_category == "Wasting_Normal":
        query = "tips status gizi anak normal pola makan sehat keseimbangan gizi " + allowed_sites
    elif prediction_category == "Wasting_Resiko Kegemukan":
        query = (
            "anak risiko kelebihan berat badan obesitas pencegahan pola makan sehat "
            "aktivitas fisik untuk anak " + allowed_sites
        )
        exact_terms = "obesitas"
    elif prediction_category == "Wasting_Sangat Kurus":
        query = (
            "wasting sangat kurus balita penyebab penanganan makanan penambah berat badan "
            + allowed_sites
        )
        exact_terms = "wasting"
    elif prediction_category == "Wasting_Kurus":
        query = (
            "wasting kurus pada anak penyebab solusi makanan bergizi penanganan wasting "
            + allowed_sites
        )
        exact_terms = "wasting"
    else:
        query = "masalah gizi pada anak pencegahan perbaikan nutrisi " + allowed_sites

    data = call_google_search_api(api_key, search_engine_id, query, exact_terms=exact_terms)
    if data and "items" in data:
        articles = []
        for item in data["items"]:
            title = item.get("title")
            link = item.get("link")
            articles.append({"title": title, "link": link})
        return articles
    else:
        return []
