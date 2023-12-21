import sys
import os
import requests

# Memeriksa apakah argumen kode telah diberikan
if len(sys.argv) < 2:
    print("Usage: python3 download.py <kode-matkul>")
    sys.exit(1)

# Mendapatkan kode dari argumen
kode = sys.argv[1]

# Membentuk URL dengan menggunakan kode
url = f"https://utthecdn.azureedge.net/exams/Naskah_{kode}_the_1.pdf"

# Direktori tujuan
destination = f"soal/{kode}/"

# Membuat direktori jika belum ada
os.makedirs(destination, exist_ok=True)

# Mengirim permintaan GET menggunakan requests
response = requests.get(url)

# Memeriksa status kode permintaan
if response.status_code == 200:
    # Mendapatkan nama file dari URL
    filename = url.split("/")[-1]

    # Menggabungkan direktori tujuan dengan nama file
    filepath = os.path.join(destination, filename)

    # Menyimpan file
    with open(filepath, "wb") as file:
        file.write(response.content)
    print("File berhasil diunduh.")
else:
    print("Gagal mengunduh file.")

