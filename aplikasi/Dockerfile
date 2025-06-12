# 1. Gunakan Python sebagai base image
FROM python:3.10-slim

# 2. Tentukan direktori kerja dalam container
WORKDIR /app

# 3. Salin semua file dari folder lokal ke dalam container
COPY . .

# 4. Install semua dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# 5. Jalankan aplikasi FastAPI menggunakan uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]