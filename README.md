# E-CV — Resya Sahroni Putri

Website E-CV berbasis Streamlit. Ikuti panduan ini sebelum dipublikasikan.

## File repository
- `app.py` — kode website
- `requirements.txt` — dependensi Streamlit
- `CV_Resya_Sahroni_Putri.pdf` — versi PDF CV untuk tombol unduh (tambahkan file ini)
- `profile.jpg` — foto profil opsional (tambahkan jika ingin digunakan)

## Cara upload ke GitHub
1. Unduh dan ekstrak ZIP ini.
2. Buka repository GitHub kamu.
3. Pilih **Add file → Upload files**.
4. Unggah `app.py` dan `requirements.txt`, serta file PDF CV yang sudah disiapkan.
5. Klik **Commit changes**.

## Mengaktifkan tombol Download CV PDF
Simpan/ekspor CV Word menjadi PDF dengan nama tepat `CV_Resya_Sahroni_Putri.pdf`, lalu unggah ke folder utama repository, sejajar dengan `app.py`.

## Menambahkan foto
Letakkan foto bernama `profile.jpg` di folder utama repository. Jika tidak ada, website menampilkan avatar ilustrasi.

## Menambahkan link Google Drive
Edit `app.py` langsung di GitHub (ikon pensil / Edit this file). Cari daftar `SEMESTERS` dan isi nilai `url` tiap semester dengan link KHS Google Drive. Cari `CERTIFICATES` dan isi nilai `url` tiap sertifikat dengan link sertifikat masing-masing. Contoh format:
`{"name": "Semester 1", "ip": "4,00", "url": "https://drive.google.com/file/d/ID_FILE/view"}`

Kosongkan URL jika tombol belum ingin ditampilkan. Pastikan akses file Google Drive adalah **Siapa saja yang memiliki link dapat melihat**.

## Personalisasi wajib sebelum dipublikasikan
- Ganti `email-kamu@example.com` dengan email yang benar.
- Tambahkan link KHS dan sertifikat.
- Periksa seluruh keahlian dan pengalaman agar sesuai dengan fakta.
- Jika teknologi pada proyek tidak sesuai, jangan menambahkannya tanpa verifikasi.
- Jangan unggah NIK, nomor KK, atau dokumen yang memuat data sensitif.
- Nilai IP semester dan IPK ditampilkan sesuai informasi yang diberikan; periksa kembali dengan KHS resmi sebelum dipublikasikan.

## Deploy ke Streamlit Community Cloud
1. Buka https://share.streamlit.io/ dan login dengan GitHub.
2. Klik **Create app**.
3. Pilih repository, branch `main`, dan main file `app.py`.
4. Klik **Deploy**.
