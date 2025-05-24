import pandas as pd

articles_df = pd.read_json('data/artikel.json')

def recommend_articles(predicted_label):
    return articles_df[articles_df['kategori'] == predicted_label].head(5).to_dict(orient='records')
