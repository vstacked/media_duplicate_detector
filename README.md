## TL;DR


This program detects duplicate files using two methods:
- ***Perceptual Hash computation***: This method is used for images and videos.
- ***SHA-256 hash***: This method is used for other file types (documents, PDFs, presentations, and text files).

The program then moves duplicate files into their respective group folders.

**How to Use:**
1. **For Video Detection**:
    - Install [ffmpeg](https://github.com/akamhy/videohash/wiki/Install-FFmpeg,-but-how%3F) on your system first.
    - Download the application from the "Releases" tab.
2. **For Other File Types:**
    - You don't need ffmpeg. Just download the application.
3. Run the program and start detecting duplicates!
***

<br>

<details>
<summary>Explanation</summary>

Deteksi Duplikasi Gambar & Video
---

Program ini ada karena awalnya saya ingin mengelompokkan file gambar dan video dari *laptop* dan *handphone* ke dalam satu tempat. Namun, dengan banyaknya file, memilah dan mengelompokkan file-file tersebut serta menentukan apakah gambar atau video sudah ada sebelumnya (duplikasi) akan memakan waktu yang lama. Maka dari itu dengan bantuan **Chat GPT** (karena saya belum terlalu familiar dengan python secara mendalam) program ini ada.

*Main program* dalam *repository* ini terdiri dari `detect8.py`, `move.py` & `delete.py`. Saya belum melakukan *refactor* atau mengoptimasi kode karena untuk saat ini yang terpenting adalah program sudah sesuai dengan ekspektasi saya, yaitu mendeteksi gambar atau video yang sama atau duplikasi. Terdapat folder `temp` yang digunakan sebagai *history* dalam proses *try and error* saat membuat program ini.

## Pembahasan

Pada langkah awal menentukan `target_folder` terlebih dahulu, kemudian *method* `group_files_by_hash` akan dijalankan, yang akan menentukan file gambar atau video berdasarkan ekstensi yang sudah ditentukan,

***

### 1. Gambar

Menggunakan *method* `get_image_hash` yang akan mendapatkan *hash*, lebih spesifiknya menggunakan __*pHash*__ atau __*Perceptual Hash computation*__. Ini menggunakan *library* [imagehash](https://scikit-image.org/) sebagai *hashing* dan [PIL](https://pillow.readthedocs.io/en/stable/) untuk mendapatkan file gambar dari path.

Sebelumnya saya menggunakan *hash* __MD5__ yang terdapat pada file `detect.py`. tapi pada praktiknya, tak jarang gambar-gambar yang tak serupa tetap masuk dalam 1 folder group yang seharusnya itu terpisah (tidak cukup akurat), lalu dengan bantuan Chat GPT terdapat note, seperti berikut

>Additionally, using the MD5 hash of the image content for comparison, which is fast but not entirely foolproof, as different images might have the same hash. For more robust duplicate image detection, you could consider using perceptual hashing techniques such as dHash or pHash.

Seperti penjelasan diatas, MD5 bisa dikatakan terlalu simple untuk membandingkan kesamaan 2 file, dan direkomendasikan dengan hasil yang __*robust*__ menggunakan __dHash__ atau __pHash__, maka dari itu pada file `detect8.py` ini menggunakan pHash. Reference [pHash](https://www.hackerfactor.com/blog/index.php?/archives/432-Looks-Like-It.html).

Lanjut, setelah hash didapatkan, maka akan melakukan pengecekan pada *dictionary* `file_groups`, terdapat *key* dengan hash tersebut atau tidak, jika ada maka akan di *append item* ke *value list* jika tidak akan membuat *key value* baru.


### 2. Video

Kemudian pada ekstensi video, saya menggunakan *libary* [videohash](https://akamhy.github.io/videohash/) yang menggunakan __pHash__ juga di dalamnya, sebelum menggunakan diperlukan menginstall __FFmpeg__ terlebih dahulu.

Setelah *hash* didapatkan, langkah yg sama dilakukan, yaitu melakukan pengecekan pada *dictionary* `file_groups`.

***


Kemudian pada langkah akhir, `file_groups` ini akan mulai di *looping* dan akan melakukan pemindahan file ke dalam group masing-masing dengan format, 

```python
f"group_{group_id}"
```

Dan lanjut ke *method* `move_single_file_folders` pada file `move.py`. Saya menentukan *target & destination folder* ke tempat yang sama, kerena saya ingin mengeluarkan file di tiap-tiap group ini yang hanya terdiri dari 1 file saja yang berarti tidak terjadi duplikasi. Dan setelah semua group sudah dilakukan pengecekan, maka *method* `delete_empty_folders` pada file `delete.py` dijalankan, yang akan menghapus folder-folder group yang kosong.

Jika semua sudah berhasil dilakukan, maka pada `target_folder` ini hanya akan tersisa folder group-group yang *duplicate* saja yang akan dilakukan pengecekan, step ini dilakukan secara manual, untuk menentukan apakah file-file di folder ini memang sama atau terdapat perbedaan, karena pada *case* dilakukan, masih ada beberapa gambar yang sebenarnya beda tapi hanya sedikit perbedaan, tapi tidak terdeteksi oleh *hash*. Setelah sudah di *filter*, maka `target_folder` saat ini sudah selesai, dan lanjut ke folder-folder yg lain yang ingin dilakukan pengecekan.

***

#### Tambahan,

Pada folder `temp`, terdapat file `index.py` & `rename.py` yang mungkin akan berguna untuk me-*rename* semua file dari `target_folder` yang ditentukan, dan juga file-file lainnya untuk saat ini belum atau tidak digunakan, karena fokus utama terdapat pada file `detect8.py`, `move.py` & `delete.py`.

Note, mungkin untuk kedepannya, jika ada keperluan lain dan memerlukan program untuk mempermudah, repository ini akan di *update* sesuai kebutuhan.

***

### Update
#### 18 April 2024
- Pada update ini saya menambahkan program dalam bentuk GUI menggunakan library __PySimpleGUI__ pada file `app2.py`, untuk file *exe* dapat dilihat pada [link berikut](https://github.com/vstacked/media_duplicate_detector/releases), tapi sebelum itu harus install __ffmpeg__ terlebih dahulu pada sistem karena diperlukan untuk library __videohash__ pada [berikut](https://github.com/akamhy/videohash/wiki/Install-FFmpeg,-but-how%3F).
- sedangkan pada file `app.py` merupakan percobaan pertama saya dalam menggunakan library ini, yang hanya menampilkan gambar dari list gambar yang dipilih.
#### 22 April 2024
- Menambahkan tipe file lain untuk di deteksi, seperti file dengan extensi `.docx`, `.pdf`, `.pptx` & `.txt` dengan menggunakan metode `hash.sha256()`
- Menambahkan tema default _GreenTan_
#### 25 April 2024
- Menambahkan pengaturan ekstensi, menambah dan menghapus ekstensi-ekstensi yang akan di *detect* agar lebih *customable*.
- Mengatur icon aplikasi dengan bantuan [AI](https://pixlr.com/image-generator).
</details>