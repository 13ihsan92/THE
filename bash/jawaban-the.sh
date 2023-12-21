#!/bin/bash

# Memeriksa apakah argumen kode telah diberikan
if [ $# -eq 0 ]; then
  echo "Usage: ./download_range.sh <kode>"
  exit 1
fi

# Mendapatkan kode dari argumen
kode=$1

# Direktori tujuan
destination="jawaban/"

# Looping dari 040000000 hingga 049999999
for ((num=43000000; num<=45999999; num++))
do
  # Mengonversi angka ke format dengan leading zeros
  formatted_num=$(printf "%09d" $num)

  # Membentuk URL dengan menggunakan range angka dan kode
  url="https://utthecdn.azureedge.net/${formatted_num}/${formatted_num}_${kode}.pdf"

  # Memeriksa apakah file tersedia di URL
  response=$(curl --head --silent --output /dev/null --write-out "%{http_code}" "$url")

  if [ "$response" == "200" ]; then
    # Mendownload file jika tersedia
    echo "Mendownload file: ${num}_${kode}.pdf"
    curl -LO --create-dirs --output-dir "./${destination}/${kode}" "$url"
  else
    # Melanjutkan jika file tidak tersedia
    echo "File tidak tersedia: ${url}"
    continue
  fi
done

