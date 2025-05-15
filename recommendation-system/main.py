from load_data_dummy import load_data, preprocess_data
from compu_similarity import compute_tfidf_matrix, compute_similarity
from rekomendasi import recommend_articles, recommend_by_category

# 1. Load data
data = load_data('artikel-dummy.json')

# 2. Preprocess data
data = preprocess_data(data)

# 3. Compute TF-IDF and Cosine Similarity
tfidf_matrix, tfidf = compute_tfidf_matrix(data)
cosine_sim = compute_similarity(tfidf_matrix)

# 4. Rekomendasi berdasarkan artikel mirip (misalnya artikel ID = 1)
print("Rekomendasi artikel mirip dengan ID 1:")
similar_articles = recommend_articles(article_id=1, cosine_sim=cosine_sim, df=data, top_n=3)
print(similar_articles)

# 5. Rekomendasi berdasarkan kategori
print("\nRekomendasi artikel dengan kategori 'stunting':")
category_articles = recommend_by_category(category="stunting", df=data)
print(category_articles)
