# Read & Brew 📚☕️

## 👥 Nama Anggota Kelompok C-08 👥
* [Muhammad Mariozulfandy](https://github.com/riozulfandy) - 2206041404
* [Patrick Samuel Evans Simanjuntak](https://github.com/patrickSevans123) - 2206028251
* [Fikri Dhiya Ramadhana](https://github.com/fikrirmdhna) - 2206819533
* [Alexander Audric Johansyah](https://github.com/audricjohansyah) - 2206815466
* [Bulan Athaillah Permata Wijaya](https://github.com/bulanath) - 2206032135

## ⏪ Latar Belakang Aplikasi ⏪
Berdasarkan studi tahun 2020, UNESCO menyatakan bahwa minat baca masyarakat Indonesia berada di angka yang sangat memprihatinkan, yakni hanya sebesar 0,001%. Dari data tersebut berarti bahwa di antara 1.000 masyarakat Indonesia, hanya ada satu orang yang rajin membaca. Selanjutnya, hasil data Asesmen Nasional (AN) tahun 2021 juga menunjukkan bahwa Indonesia mengalami darurat literasi karena 1 dari 2 peserta didik masih belum mencapai kompetensi minimum literasi.

Sebagai salah satu cara untuk mengatasi masalah di atas, kami memutuskan untuk membuat aplikasi **Read & Brew**. **Read & Brew** merupakan sebuah aplikasi yang memadukan kegemaran akan buku dengan kenyamanan sebuah kafe. Kami memiilih kafe sebagai sarana untuk meningkatkan tingkat literasi karena adanya peningkatan yang signifikan terkait dengan tingkat pengunjung kafe di kalangan anak muda. Kami memiliki harapan bahwa kafe tidak hanya bisa menjadi tempat untuk bersantai, tetapi juga menjadi sarana untuk meningkatkan literasi dari kalangan muda yang mayoritasnya masih memiliki tingkat literasi yang rendah.

## 💡 Daftar Modul Aplikasi 💡
### 1. Book List (Muhammad Mariozulfandy)
Berisi daftar buku-buku yang diambil dari dataset. Setiap data buku pada dataset yang digunakan akan ditampilkan beserta rating yang diperoleh pada modul Forum Review. Daftar buku-buku juga akan dapat dibagi berdasarkan kategori dan terdapat fitur search bar untuk mencari buku tertentu.
#### Peran Role Pengguna
| Member (Login)  | Employee  | Guest |
| ------------- | ------------- | ------------- |
| Dapat melihat daftar buku-buku beserta ratingnya.  | Dapat menambahkan buku baru.  | Dapat melihat daftar buku-buku tapi tidak dapat melihat rating yang telah diberikan pada buku tersebut.  |
### 2. Book Tracker & Planner (Bulan Athaillah Permata Wijaya)
Buku yang sedang dipinjam dapat di-_track progressnya_ dengan menandai sudah sejauh mana buku dibaca. Selain itu, pengguna dapat mengelompokkan buku-buku yang ingin dibaca ke dalam _book planner_ sesuai dengan preferensinya.
#### Peran Role Pengguna
| Member (Login)  | Guest |
| ------------- | ------------- |
| Dapat melakukan _tracking progress_ buku bacaan yang dipinjam dan dapat menggunakan fitur _book planner_. | Dapat melakukan _tracking progress_ disaat berkunjung saja serta tidak dapat menggunakan fitur _book planner_. |
### 3. Forum Review (Fikri Dhiya Ramadhana)
Pengguna dapat me-review buku yang sudah dipinjam dan membagikan pengalaman saat menggunakan aplikasi Read&Brew. Digunakan sistem rating untuk setiap pengalaman user. 
#### Peran Role Pengguna
| Member (Login)  | Guest |
| ------------- | ------------- |
| Member dapat menulis review dari buku yang dipinjam dan menceritakan pengalaman user, lalu review akan di simpan ke dalam sistem. | User hanya bisa mengirim feedback secara anonim, jika ingin menulis review dan membagikan pengalamannya maka akan di-direct ke sign up page. |

### 4. Order & Borrow (Alexander Audric Johansyah)
Pengguna dapat memesan berbagai jenis makanan dan minuman yang tersedia di menu cafe Read & Brew. Setelah pengguna memesan makanan dan minuman, pengguna dapat meminjam buku yang tersedia pada katalog buku.

| Member (Login)  | Employee | Guest |
| ------------- | ------------- | ------------- |
| Member dapat memesan makanan dan meminjam buku | Employee dapat memeriksa *inventory* dalam cafe | Guest hanya dapat memesan makanan

### 5. Book Request (Patrick Samuel Evans Simanjuntak)
Pengguna dapat meminta pengelola kafe untuk menambahkan buku-buku yang dirasa menarik dan dibutuhkan oleh pengguna. 
| Member (Login)  | Employee | Guest |
| ------------- | ------------- | ------------- |
| Member membuat *request* buku dan menyukai *request* buku| Employee dapat menyetujui *request* buku | Guest tidak bisa mengakses halaman *book request*.

## ℹ Sumber Dataset Katalog Buku ℹ
Sumber dataset buku = https://github.com/uchidalab/book-dataset/blob/master/Task2/book32-listing.csv

Dataset akan dilakukan prapemprosesan terlebih dahulu dengan Pandas untuk memilih dan memilah data yang akan dimasukkan ke aplikasi. Diambil total 320 data dari dataset tersebut. Link Notebook dan dataset yang telah di preproses:
https://drive.google.com/drive/folders/1hx7s5vcN59ihvJnt7NNN-X0zln6Abdbr?usp=sharing

## 👱‍♂️ Role Pengguna Aplikasi 👩
### 1. Seluruh Pelanggan Cafe (Guest)
### 2. Pelanggan Cafe yang Mendaftar pada Aplikasi (Member)
### 3. Pengelola Cafe (Employee)