from sklearn.feature_extraction.text import TfidfVectorizer
from Sastrawi.StopWordRemover.StopWordRemoverFactory import StopWordRemoverFactory # type: ignore
from load_data_dummy import load_data, preprocess_data
def compute_tfidf_matrix(df, text_column='text'):
    '''Ambil daftar stop words bahasa Indonesia dari Sastrawi'''
    factory = StopWordRemoverFactory()
    stop_words = factory.get_stop_words()

    '''Inisialisasi TF-IDF Vectorizer'''
    tfidf = TfidfVectorizer(stop_words=stop_words)

    '''Hitung TF-IDF matrix dari kolom teks'''
    tfidf_matrix = tfidf.fit_transform(df[text_column])
    
    return tfidf_matrix, tfidf
from sklearn.metrics.pairwise import cosine_similarity

def compute_similarity(tfidf_matrix):
    '''Menghitung cosine similarity antar artikel'''
    cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)
    return cosine_sim

df = load_data("artikel-dummy.json")
df = preprocess_data(df)

'''Hitung Cosine Similarity'''
tfidf_matrix, tfidf = compute_tfidf_matrix(df, text_column='text')
cosine_sim = compute_similarity(tfidf_matrix)