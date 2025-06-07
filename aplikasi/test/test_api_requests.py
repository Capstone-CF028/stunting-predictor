import requests

base_url = "http://127.0.0.1:8000"

print("Masukkan data anak untuk prediksi stunting & wasting serta rekomendasi artikel:\n")

# Input data dari pengguna
gender = int(input("1. Jenis Kelamin (0 = Perempuan, 1 = Laki-laki): "))
age_months = int(input("2. Usia Anak (dalam bulan): "))
height_cm = float(input("3. Tinggi Badan (cm): "))
weight_kg = float(input("4. Berat Badan (kg): "))

input_data = [gender, age_months, height_cm, weight_kg]

# Validasi jumlah fitur
expected_length = 4
if len(input_data) != expected_length:
    print(f"❌ Jumlah fitur input salah! Diperlukan {expected_length} fitur.")
    exit()

# Kirim request ke endpoint gabungan
print("\nMengirim data ke server...")
response = requests.post(
    f"{base_url}/predict-and-recommend",
    json={"data": input_data}
)

# Tampilkan hasil
print("\n[Hasil Prediksi & Rekomendasi]")
try:
    result = response.json()
    print(f"\nStunting: {result.get('stunting')}")
    print(f"Wasting: {result.get('wasting')}")
    print(f"Kategori Gabungan: {result.get('combined_category')}")
    print("\nArtikel Rekomendasi:")
    for i, article in enumerate(result.get('articles', []), 1):
        print(f"{i}. {article['title']}\n   {article['link']}")
except Exception as e:
    print("❌ Gagal parsing response JSON:", e)
    print("Response mentah:", response.text)