#!/usr/bin/env python3

import sys
import os
import requests

# Memeriksa apakah argumen kode telah diberikan
if len(sys.argv) < 2:
    print("Usage: python3 download_range.py <kode>")
    sys.exit(1)

# Mendapatkan kode dari argumen
kode = sys.argv[1]

# Direktori tujuan
destination = "jawaban/"

# Membuat direktori jika belum ada
os.makedirs(destination, exist_ok=True)

# Looping dari 43000000 hingga 45999999
for num in range(43000000, 46000000):
    # Mengonversi angka ke format dengan leading zeros
    formatted_num = str(num).zfill(9)

    # Membentuk URL dengan menggunakan range angka dan kode
    url = f"https://utcdn.azureedge.net/{formatted_num}/{formatted_num}_{kode}.pdf"

    # Memeriksa apakah file tersedia di URL
    response = requests.head(url)

    if response.status_code == 200:
        # Mendownload file jika tersedia
        print(f"Mendownload file: {formatted_num}_{kode}.pdf")
        filepath = os.path.join(destination, kode, f"{formatted_num}_{kode}.pdf")
        response = requests.get(url)
        with open(filepath, "wb") as file:
            file.write(response.content)
    else:
        # Melanjutkan jika file tidak tersedia
        print(f"File tidak tersedia: {url}")
        continue

