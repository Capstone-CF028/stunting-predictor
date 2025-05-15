from load_data_dummy import load_data
import pandas as pd

# Supaya isi panjang ditampilkan penuh
pd.set_option('display.max_colwidth', None)

def recommend_articles(article_id, cosine_sim, df, top_n=5):
    # Mengambil indeks artikel yang dimaksud
    if article_id not in df['id'].values:
        raise ValueError("ID artikel tidak ditemukan.")
    idx = df[df['id'] == article_id].index[0]
    

    # Mengambil pairwise similarity scores untuk artikel yang diberikan
    sim_scores = list(enumerate(cosine_sim[idx]))
    
    # Mengurutkan artikel berdasarkan similarity score (dari tinggi ke rendah)
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    
    # Mengambil n artikel teratas
    sim_scores = sim_scores[1:top_n+1]  # Skipping the input article itself
    
    # Mengambil indeks artikel yang paling mirip
    article_indices = [i[0] for i in sim_scores]
    
    return df.iloc[article_indices][['judul', 'isi',]]

def recommend_by_category(category, df):
    # Menyaring artikel berdasarkan kategori
    recommended_articles = df[df['kategori'] == category]
    return recommended_articles[[ 'judul', 'isi']]

