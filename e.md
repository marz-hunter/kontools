Anda dapat menggunakan script bash berikut untuk menggabungkan "security@" ke baris pertama dalam setiap baris di file.txt:

```bash
#!/bin/bash

file="file.txt"

while IFS= read -r line; do
    echo "security@${line}"
done < "$file"
```

Simpan script di atas dalam sebuah file dengan ekstensi `.sh`, misalnya `add_security.sh`. Pastikan file.txt berada di direktori yang sama dengan script tersebut. Kemudian, berikan izin eksekusi pada script dengan perintah `chmod +x add_security.sh`.

Setelah itu, jalankan script dengan menggunakan perintah `./add_security.sh`. Output akan ditampilkan di terminal atau bisa dialihkan ke file lain jika diinginkan.

Misalnya, jika file.txt berisi:

```
google.com
aiza.com
```

Maka output yang dihasilkan akan menjadi:

```
security@google.com
security@aiza.com
```

Semoga membantu!
