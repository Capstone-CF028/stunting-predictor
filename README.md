# Stunting Predictor

**Capstone Project – Tim CF028**  
Aplikasi prediksi stunting berbasis FastAPI (Python) + ML + frontend (Vite)

---

## Deskripsi

Aplikasi ini memprediksi apakah seorang anak berisiko stunting berdasarkan data jenis kelamin, tinggi badan, berat badan dan usia anak
Dengan tambahan, tool ini memberikan rekomendasi artikel menggunakan Google Custom Search API.

---

## Fitur Utama

- **Backend**: FastAPI + model ML (Keras/TensorFlow) + standar scaler (joblib)
- **Endpoint**:
  - `POST /predict/stunting`
  - `POST /predict/wasting`
  - `POST /predict-and-recommend`
  - `GET /` (status)
- **Frontend**: Single Page aplikasi (HTML, ES Modules, Vite dev server)
- **Rekomendasi**: Hasil query dari Google Custom Search API

---

## Prasyarat

Pastikan sudah terinstall:

- Python 3.9+ (disarankan gunakan virtualenv)
- Node.js & npm/yarn
- API key Google Custom Search (Cloud Console)
- Git

---

## Langkah-langkah Instalasi & Menjalankan

### 1. Clone Repository  
```bash
git clone https://github.com/Capstone-CF028/stunting-predictor.git
cd stunting-predictor
```

### 2. Setup Backend (Python)

```bash
cd backend
python3 -m venv venv
source venv/bin/activate             # Linux/macOS
venv\Scripts\activate                # Windows
pip install -r requirements.txt
```

Tambahkan file `.env` di folder `backend` seperti berikut:

```
API_KEY=YOUR_GOOGLE_API_KEY
SEARCH_ENGINE_ID=YOUR_SEARCH_ENGINE_ID
```

### 3. Jalankan Backend FastAPI

```bash
uvicorn app.main:app --reload
```

- API akan berjalan pada `http://localhost:8000`
- FastAPI akan menyediakan Swagger UI di `http://localhost:8000/docs`

---

### 4. Setup Frontend (Vite + ES Modules)

```bash
cd ../frontend
npm install          # atau yarn install
npm run dev          # atau yarn dev
```

- Frontend akan berjalan di `http://localhost:5175`
- CORS di backend sudah mengizinkan origin `http://localhost:5175`

---

## Penggunaan

- Buka: `http://localhost:5175` di browser
- Isi form prediksi
- Tekan tombol untuk melihat prediksi & rekomendasi nutrisi

---

## Cara Berkontribusi

1. Fork repo ini  
2. Buat branch: `git checkout -b feature/xyz`  
3. Commit perubahan dengan jelas  
4. Push: `git push origin feature/xyz`  
5. Buat **Pull Request**  

> Pastikan menambahkan unit test jika mengubah logika backend, atau screenshot jika mengubah UI.

---

### Catatan untuk Pengembang

- Tambahkan `.gitignore` untuk `venv/`, `node_modules/`, `.env`, dsb.
- Pastikan environment `.env` lengkap agar rekomendasi artikel bekerja.
- Perlu tambahkan validasi form jika input belum lengkap.
- `requirements.txt` minimal mencakup: FastAPI, uvicorn, tensorflow, joblib, pandas, numpy, requests, python-dotenv.

---

