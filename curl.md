Anda dapat menggunakan script bash berikut ini untuk menambahkan "http://0.0.0.0:8085/" di depan setiap nama file dalam folder tersebut:

```bash
#!/bin/bash

# Ganti direktori ke folder yang berisi file-file javascript
cd /path/to/your/js/files

# Loop melalui setiap file dengan ekstensi .js dalam folder saat ini
for file in *.js; do
  # Buat nama file lengkap dengan alamat yang diinginkan
  new_name="http://0.0.0.0:8085/$file"
  
  # Cetak nama file baru ke layar (opsional, dapat dihilangkan)
  echo $new_name
  
  # Pindahkan/rename file dengan nama baru
  mv "$file" "$new_name"
done
```

Pastikan untuk mengganti "/path/to/your/js/files" dengan jalur lengkap ke folder yang berisi file-file JavaScript. Setelah Anda menyimpan script di dalam file (misalnya "rename_js_files.sh"), berikan izin eksekusi dengan menjalankan perintah berikut:

```bash
chmod +x rename_js_files.sh
```

Kemudian, jalankan script tersebut dengan:

```bash
./rename_js_files.sh
```

Dengan begitu, setiap file JavaScript dalam folder tersebut akan direname dengan menambahkan "http://0.0.0.0:8085/" di depan nama file.
