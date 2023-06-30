Anda dapat menggunakan script bash berikut untuk menghasilkan output yang diinginkan:

```bash
#!/bin/bash

filename="file.txt"

while IFS= read -r line
do
  echo "print $line | curl -s 'http://127.0.0.1:8880/?email=$line' | jq"
  echo "sleep 1"
done < "$filename"
```

Simpan script di atas dalam file dengan ekstensi `.sh`, misalnya `generate_curl.sh`. Kemudian, buka terminal dan navigasikan ke direktori tempat Anda menyimpan file tersebut. Jalankan perintah berikut untuk memberikan izin eksekusi pada script:

```bash
chmod +x generate_curl.sh
```

Terakhir, jalankan script dengan perintah:

```bash
./generate_curl.sh
```

Anda akan melihat output yang menghasilkan perintah curl dan sleep sesuai dengan konten file `file.txt`.
