import json
import pandas as pd

def load_data(json_file):
    with open(json_file, 'r') as f:
        data = json.load(f)
        df = pd.DataFrame(data)
    return df

def preprocess_data(df):
    '''Menggabungkan judul dan isi ke dalam variabel text untuk menghitung matriks TF-IDF'''
    df['text'] = (
        df['judul'] + ' ' + 
        df['isi'] + ' ' + 
        df['kategori'] + ' ' + 
        df['tag'].apply(lambda tags: ' '.join(tags))
    )
    return df