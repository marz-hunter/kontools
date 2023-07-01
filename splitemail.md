Anda dapat menggunakan script bash berikut untuk menggabungkan alamat email dalam setiap file menjadi satu baris, dipisahkan oleh koma, dan menyimpannya kembali ke file asal:

```bash
#!/bin/bash

# Mendapatkan daftar file di folder
files=$(find /path/to/folder -type f)

# Melakukan iterasi untuk setiap file
for file in $files; do
  # Memproses file hanya jika memiliki ekstensi .txt
  if [[ $file == *.txt ]]; then
    # Menggabungkan alamat email menjadi satu baris, dipisahkan oleh koma
    emails=$(awk '{ORS=NR%2?",":"\n"} 1' "$file")

    # Menyimpan alamat email yang digabungkan ke file asal
    echo "$emails" > "$file"
  fi
done
```

Pastikan untuk mengganti `/path/to/folder` dengan jalur folder yang berisi file-file Anda. Script ini akan mencari semua file di dalam folder tersebut dan menggabungkan alamat email dalam file yang memiliki ekstensi `.txt` menjadi satu baris, dipisahkan oleh koma. Hasilnya akan ditulis kembali ke file asal.

Penting untuk dicatat bahwa script ini mengasumsikan bahwa setiap file dalam folder hanya berisi dua baris yang berisi alamat email. Jika ada perbedaan dalam format file atau lebih dari dua baris dalam setiap file, script ini mungkin tidak berfungsi dengan benar. Pastikan juga bahwa Anda memiliki izin untuk membaca, menulis, dan mengubah file-file di folder tersebut sebelum menjalankan script ini.
