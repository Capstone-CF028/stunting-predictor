import pandas as pd
import re
import pickle
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory
from Sastrawi.StopWordRemover.StopWordRemoverFactory import StopWordRemoverFactory

# =============================
# 1. Load dan Preprocess Data
# =============================

def load_data(file_path):
    return pd.read_json(file_path)

def preprocess_data(df):
    # Kombinasikan judul dan isi
    df['text'] = df['judul'] + " " + df['isi']
    
    # Bersihkan teks & stemming
    factory = StemmerFactory()
    stemmer = factory.create_stemmer()

    def clean_text(text):
        text = re.sub(r'[^\w\s]', '', text.lower())  # lowercase & hapus tanda baca
        return stemmer.stem(text)

    df['text'] = df['text'].apply(clean_text)
    return df

# =============================
# 2. TF-IDF & Cosine Similarity
# =============================

def compute_tfidf_matrix(df, text_column='text'):
    factory = StopWordRemoverFactory()
    stop_words = factory.get_stop_words()
    tfidf = TfidfVectorizer(stop_words=stop_words)
    tfidf_matrix = tfidf.fit_transform(df[text_column])
    return tfidf_matrix, tfidf

def compute_similarity(tfidf_matrix):
    cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)
    return cosine_sim

# =============================
# 3. Rekomendasi
# =============================

def recommend_articles(article_id, cosine_sim, df, top_n=5):
    if article_id not in df['id'].values:
        raise ValueError("ID artikel tidak ditemukan.")
    
    idx = df[df['id'] == article_id].index[0]
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores[1:top_n+1]
    article_indices = [i[0] for i in sim_scores]
    return df.iloc[article_indices][['id', 'judul', 'isi']]

def recommend_by_category(category, df):
    return df[df['kategori'].str.lower() == category.lower()][['id', 'judul', 'isi']]

# =============================
# 4. Main Program
# =============================

def main():
    # 1. Load & Preprocess
    data = load_data('artikel-dummy.json')
    data = preprocess_data(data)

    # 2. TF-IDF dan Similarity
    tfidf_matrix, tfidf = compute_tfidf_matrix(data)
    cosine_sim = compute_similarity(tfidf_matrix)

    # 3. Simpan model dan data
    with open('model_tfidf.pkl', 'wb') as f:
        pickle.dump(tfidf, f)
    with open('cosine_similarity.pkl', 'wb') as f:
        pickle.dump(cosine_sim, f)
    data.to_json('data_preprocessed.json', orient='records', indent=2)

    # 4. Contoh Output
    print("Rekomendasi artikel mirip dengan ID 1:")
    similar = recommend_articles(article_id=1, cosine_sim=cosine_sim, df=data, top_n=3)
    print(similar)

    print("\nRekomendasi artikel dengan kategori 'stunting':")
    by_category = recommend_by_category("stunting", data)
    print(by_category)

# Jalankan
if __name__ == "__main__":
    main()
