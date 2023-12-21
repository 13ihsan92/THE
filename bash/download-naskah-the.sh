#!/bin/bash

# Memeriksa apakah argumen kode telah diberikan
if [ $# -eq 0 ]; then
  echo "Usage: bash ./download <kode-matkul>"
  exit 1
fi

# Mendapatkan kode dari argumen
kode=$1

# Membentuk URL dengan menggunakan kode
url="https://utthecdn.azureedge.net/exams/Naskah_${kode}_the_1.pdf"

# Direktori tujuan
destination="soal/"

# Mendownload file menggunakan curl & membuat direktori jika belum ada
curl -LO --create-dirs --output-dir "./${destination}/${kode}" "$url"

