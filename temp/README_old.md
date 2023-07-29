Deteksi duplikasi image & video

Program ini ada karena pada awalnya saya ingin grouping file image & video, yang merupakan gabungan file-file dari device laptop dan handphone. ketika semua sudah menjadi di 1 tempat, dengan begitu banyaknya file, akan memakan waktu lama utk memilah file-file utk di kelompokkan serta menentukan apakah gambar atau video ini sudah ada sebelumnya atau tidak (duplicate), maka dari itu dengan bantuan Chat GPT (karena saya blm terlalu familiar dengan python secara mendalam) program ini ada.

main program pada repo ini adalah detect8.py move.py delete.py, kenapa tidak saya rename atau ubah struktur kode ataupun di optimalisasi, karena untuk saat ini yang terpenting program sudah sesuai ekspetasi saya yaitu mendeteksi gambar atau video yg sama/duplikasi. dan terdapat folder temp, merupakan sebagai history saya dalam try and error dalam membuat program ini.

masuk ke pembahasan,

pada langkah awal menentukan target_folder terlebih dahulu, kemudian method group_files_by_hash akan dijalankan, yang akan menentukan file image/video berdasarkan ekstensi yang sudah ditentukan,

1. gambar
ketika kondisi pertama ini true, maka akan memanggil method get_image_hash yang akan mendapatkan hash, lebih spesifiknya menggunakan phash atau Perceptual Hash computation. ini menggunakan library https://scikit-image.org/ sebagai hashing dan https://pillow.readthedocs.io/en/stable/ untuk mendapatkan file image dari path

sebelumnya saya menggunakan hash md5 yang terdapat pada file detect.py,dan pada realitanya, waktu percobaan, tak jarang gambar-gambar yang tak serupa tetap masuk dalam 1 folder group yang seharusnya itu terpisah, lalu pada dengan bantuan chat GPT terdapat note, seperti berikut

Additionally, using the MD5 hash of the image content for comparison, which is fast but not entirely foolproof, as different images might have the same hash. For more robust duplicate image detection, you could consider using perceptual hashing techniques such as dHash or pHash.

seperti penjelasan diatas, MD5 bisa dikatakan terlalu simple untuk mengcompare kesamaan 2 file, dan direkomendasikan dengan hasil yang robust menggunakan dHash atau pHash, maka dari itu pada file detect8.py ini menggunakan phash. reference https://www.hackerfactor.com/blog/index.php?/archives/432-Looks-Like-It.html

lanjut, setelah hash didapatkan, maka akan melakukan pengecekan pada dictionary file_groups, terdapat key dengan hash tersebut atau tidak, jika ada maka akan di append item ke value list jika tidak akan membuat key value baru.

2. video
kemudian ketika kondisi ini true, dengan ekstensi video, kali ini saya menggunakan libary videhash https://akamhy.github.io/videohash/ yang menggunakan phash juga di dalamnya, sebelum menggunakan diperlukan menginstall FFmpeg terlebih dahulu.

setelah hash didapatkan, langkah yg sama dilakukan, yaitu melakukan pengecekan pada dictionary file_groups

kemudian pada langkah akhir, file_groups ini akan mulai di looping dan akan melakukan pemindahan file ke dalam group masing-masing dengan format group_{group_id}

dan lanjut ke method move_single_file_folders pada file move.py. saya menentukan target & destination folder ke tempat yang sama, kerena saya ingin mengeluarkan file di tiap-tiap group ini yang hanya terdiri dari 1 file saja yang berarti tidak terjadi duplikasi. dan setelah semua group sudah dilakukan pengecekan, maka method delete_empty_folders pada file delete.py dijalankan, yang akan menghapus folder-folder group yang kosong

jika semua sudah berhasil dilakukan, maka pada target_folder ini hanya akan tersisa folder group-group yang duplicate saja yang akan dilakukan pengecekan, step ini saya lakukan secara manual, untuk menentukan apakah file-file di folder ini memang sama atau terdapat perbedaan, karena pada case saya lakukan, masih ada beberapa gambar yang sebenarnya beda tapi hanya sedikit perbedaan, tapi pada hash di dianggap sama. setelah sudah di filter, maka target_folder saat ini sudah selesai, dan lanjut ke folder-folder yg lain yang saya ingin lakukan pengecekan.


tambahan,
pada folder temp, ada file index.py rename.py yang mungkin akan berguna untuk me-rename semua file dari target_folder yang ditentukan, dan file-file selain itu untuk saat ini belum saya gunakan, karena di sisi lain, final program pada repo ini terdapat pada file detect8.py move.py delete.py

note
mungkin untuk kedepannya, jika ada keperluan lain dan memerlukan program untuk mempermudah, repo ini akan saya update sesuai kebutuhan