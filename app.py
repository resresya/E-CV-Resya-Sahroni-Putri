import streamlit as st
from pathlib import Path
import base64

st.set_page_config(
    page_title="E-CV | Resya Sahroni Putri",
    page_icon="💼",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ==========================================================
# DATA E-CV
# Ganti email, nomor kontak, dan tautan Google Drive di sini.
# Pastikan kemampuan dan pengalaman yang dicantumkan benar.
# ==========================================================
PROFILE = {
    "name": "Resya Sahroni Putri",
    "role": "Mahasiswa S1 Sistem Informasi",
    "university": "Universitas Bina Sarana Informatika Yogyakarta",
    "tagline": "Belajar, Berkembang, dan Membangun Solusi Digital",
    "about": (
        "Mahasiswa Program Studi Sistem Informasi Universitas Bina Sarana Informatika "
        "Yogyakarta. Memiliki minat pada pengembangan sistem informasi, basis data, dan "
        "teknologi digital. Berpengalaman mengikuti Praktik Kerja Lapangan di bidang "
        "fotografi serta aktif sebagai Staf Publikasi dan Dokumentasi (PDD) Himpunan "
        "Mahasiswa Sistem Informasi. Terus mengembangkan kompetensi melalui proyek, "
        "seminar, dan sertifikasi profesional."
    ),
    "email": "email-kamu@example.com",
    "whatsapp": "",  # Opsional, contoh format: https://wa.me/6281234567890
    "ipk": "3,96 / 4,00",
}

# Tempel link Google Drive KHS masing-masing semester.
SEMESTERS = [
    {"name": "Semester 1", "ip": "4,00", "url": ""},
    {"name": "Semester 2", "ip": "3,84", "url": ""},
    {"name": "Semester 3", "ip": "4,00", "url": ""},
    {"name": "Semester 4", "ip": "4,00", "url": ""},
]

SKILLS_HARD = [
    "HTML", "CSS", "PHP", "SQL", "MySQL / MariaDB",
    "Database Design", "Figma", "Microsoft Office", "Visual Studio Code"
]
SKILLS_SOFT = [
    "Komunikasi", "Kerja Sama Tim", "Problem Solving",
    "Disiplin", "Cepat Belajar", "Bertanggung Jawab"
]

EXPERIENCES = [
    {
        "title": "Praktik Kerja Lapangan",
        "place": "KOI Photography",
        "items": [
            "Melayani pelanggan selama sesi pemotretan.",
            "Berkomunikasi dengan klien untuk memahami kebutuhan.",
            "Membantu proses dokumentasi dan pengelolaan hasil foto.",
            "Bekerja sama dengan tim dalam pelaksanaan kegiatan.",
        ],
    },
    {
        "title": "Staf Publikasi dan Dokumentasi (PDD)",
        "place": "Himpunan Mahasiswa Sistem Informasi",
        "items": [
            "Mendokumentasikan kegiatan organisasi.",
            "Membantu pembuatan publikasi kegiatan.",
            "Berkolaborasi dalam pelaksanaan kegiatan mahasiswa.",
        ],
    },
]

PROJECTS = [
    {
        "title": "Digitalisasi Pendaftaran Pasien pada Klinik untuk Meningkatkan Efektivitas Layanan Berbasis Web dengan Metode RAD",
        "method": "Rapid Application Development (RAD)",
        "description": [
            "Analisis kebutuhan sistem.",
            "Perancangan basis data dan antarmuka pengguna.",
            "Pengembangan sistem pendaftaran pasien berbasis web.",
        ],
    },
    {
        "title": "Sistem Informasi Manajemen Penjualan Toko Sayur Berbasis Web Menggunakan Metode Design Thinking",
        "method": "Design Thinking",
        "description": [
            "Analisis kebutuhan pengguna.",
            "Perancangan sistem informasi.",
            "Perancangan solusi untuk mendukung pengelolaan penjualan.",
        ],
    },
]

# Tempel link Google Drive setiap dokumen pada kolom url.
CERTIFICATES = [
    {"title": "Database Administrator – BNSP", "category": "Sertifikasi Kompetensi", "url": ""},
    {"title": "Uji Kompetensi Berbasis Industri Bidang Basis Data", "category": "Sertifikasi Kompetensi", "url": ""},
    {"title": "Software Quality Assurance", "category": "Sertifikasi Kompetensi", "url": ""},
    {"title": "Seminar Wajib Entrepreneur", "category": "Seminar", "url": ""},
    {"title": "Seminar Sosial Pencegahan Intoleransi, Radikalisme, dan Terorisme di Lingkungan Kampus", "category": "Seminar", "url": ""},
    {"title": "Akselerasi Transformasi Digital Mendukung Ekonomi Kreatif Melalui Talenta Digital", "category": "Seminar", "url": ""},
    {"title": "Webinar Edukasi & Inklusi Pasar Modal", "category": "Webinar", "url": ""},
    {"title": "Panitia Workshop Pemanfaatan Artificial Intelligence (AI)", "category": "Kepanitiaan", "url": ""},
]

# Tempatkan CV PDF bernama CV_Resya_Sahroni_Putri.pdf di folder yang sama.
PDF_PATH = Path(__file__).parent / "CV_Resya_Sahroni_Putri.pdf"
PHOTO_PATH = Path(__file__).parent / "profile.jpg"

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');
html, body, [class*="css"] {font-family:Inter,sans-serif;}
.stApp {background:radial-gradient(circle at 50% 0%,#1d2a52 0%,#0b1020 42%,#080c18 100%);color:#edf2ff;}
.block-container {max-width:1050px;padding-top:1.5rem;padding-bottom:4rem;}
.hero {text-align:center;padding:2.2rem 1rem 1.6rem;}
.avatar {width:125px;height:125px;margin:0 auto 1.2rem;border-radius:50%;display:flex;align-items:center;justify-content:center;font-size:3rem;background:linear-gradient(135deg,#263e78,#743ce5);border:3px solid #8b7bff;box-shadow:0 0 35px #5b61df55;}
.eyebrow {display:inline-block;padding:.5rem 1rem;border:1px solid #5c4bc2;border-radius:999px;color:#c3a8ff;background:#241c4388;font-size:.85rem;font-weight:700;margin-bottom:1.1rem;}
.name {font-size:clamp(2.2rem,6vw,4rem);font-weight:800;letter-spacing:-1.5px;line-height:1.1;margin:.3rem 0 1rem;background:linear-gradient(90deg,#4b9bff,#9a62ff);-webkit-background-clip:text;-webkit-text-fill-color:transparent;}
.role {color:#c2cce0;font-size:1.15rem;font-weight:600;}
.tagline {color:#65a6ff;font-size:1rem;font-style:italic;margin-top:.7rem;}
.section-title {font-size:1.6rem;font-weight:800;margin:2.3rem 0 1rem;color:#f4f6ff;}
.card {background:linear-gradient(135deg,#151e33dd,#101729ee);border:1px solid #293653;border-radius:17px;padding:1.15rem 1.25rem;margin-bottom:1rem;height:100%;}
.card h3 {margin:0 0 .45rem;color:#a991ff;font-size:1.04rem;line-height:1.45;}
.muted {color:#a6b3c9;font-size:.9rem;}
.pill {display:inline-block;padding:.38rem .72rem;margin:.18rem .2rem .18rem 0;border-radius:999px;border:1px solid #3c4d76;background:#1b2945;color:#c7d8ff;font-size:.82rem;}
.big-ipk {font-size:2rem;font-weight:800;color:#a991ff;}
a {color:#8bb8ff !important;}
div.stDownloadButton > button {border:1px solid #4a5880;border-radius:12px;background:#17213a;color:#fff;}
.footer {text-align:center;color:#8290aa;padding-top:2rem;font-size:.82rem;}
</style>
""", unsafe_allow_html=True)

# Hero
st.markdown('<div class="hero">', unsafe_allow_html=True)
if PHOTO_PATH.exists():
    encoded = base64.b64encode(PHOTO_PATH.read_bytes()).decode()
    st.markdown(f'<img src="data:image/jpeg;base64,{encoded}" style="width:140px;height:140px;object-fit:cover;border-radius:50%;border:3px solid #8292ff;box-shadow:0 0 35px #5b61df55;margin-bottom:20px;">', unsafe_allow_html=True)
else:
    st.markdown('<div class="avatar">👩🏻‍💻</div>', unsafe_allow_html=True)
st.markdown('<div class="eyebrow">✦ DIGITAL CURRICULUM VITAE</div>', unsafe_allow_html=True)
st.markdown(f'<div class="name">{PROFILE["name"]}</div>', unsafe_allow_html=True)
st.markdown(f'<div class="role">{PROFILE["role"]}</div>', unsafe_allow_html=True)
st.markdown(f'<div class="muted">{PROFILE["university"]}</div>', unsafe_allow_html=True)
st.markdown(f'<div class="tagline">“{PROFILE["tagline"]}”</div>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# PDF button
if PDF_PATH.exists():
    st.download_button("📄 Download CV (PDF)", data=PDF_PATH.read_bytes(),
                       file_name="CV_Resya_Sahroni_Putri.pdf", mime="application/pdf",
                       use_container_width=True)
else:
    st.info("Untuk mengaktifkan tombol Download CV (PDF), unggah file CV_Resya_Sahroni_Putri.pdf ke repository GitHub bersama app.py.")

st.markdown('<div class="section-title">👋 Tentang Saya</div>', unsafe_allow_html=True)
st.markdown(f'<div class="card">{PROFILE["about"]}</div>', unsafe_allow_html=True)

st.markdown('<div class="section-title">🎓 Pendidikan & Prestasi Akademik</div>', unsafe_allow_html=True)
st.markdown(f'<div class="card"><div class="muted">IPK Kumulatif</div><div class="big-ipk">{PROFILE["ipk"]}</div><div>{PROFILE["university"]}</div><div class="muted">S1 Sistem Informasi · 2024–Sekarang</div></div>', unsafe_allow_html=True)
cols = st.columns(4)
for col, sem in zip(cols, SEMESTERS):
    with col:
        st.markdown(f'<div class="card"><div class="muted">{sem["name"]}</div><div class="big-ipk">{sem["ip"]}</div></div>', unsafe_allow_html=True)
        if sem["url"].strip():
            st.link_button("📄 Lihat KHS", sem["url"], use_container_width=True)
        else:
            st.caption("Tambahkan link KHS di kode")
st.markdown('<div class="card"><h3>SMK Negeri 1 Pengasih</h3><div>Jurusan Multimedia · Lulus 2024</div></div>', unsafe_allow_html=True)

st.markdown('<div class="section-title">🛠️ Keahlian</div>', unsafe_allow_html=True)
c1, c2 = st.columns(2)
with c1:
    st.markdown('<div class="card"><h3>Hard Skill</h3>' + ''.join(f'<span class="pill">{s}</span>' for s in SKILLS_HARD) + '</div>', unsafe_allow_html=True)
with c2:
    st.markdown('<div class="card"><h3>Soft Skill</h3>' + ''.join(f'<span class="pill">{s}</span>' for s in SKILLS_SOFT) + '</div>', unsafe_allow_html=True)

st.markdown('<div class="section-title">💼 Pengalaman</div>', unsafe_allow_html=True)
for exp in EXPERIENCES:
    st.markdown(f'<div class="card"><h3>{exp["title"]}</h3><div class="muted">{exp["place"]}</div><ul>' + ''.join(f'<li>{item}</li>' for item in exp["items"]) + '</ul></div>', unsafe_allow_html=True)

st.markdown('<div class="section-title">💻 Proyek & Portofolio</div>', unsafe_allow_html=True)
for project in PROJECTS:
    st.markdown(f'<div class="card"><h3>{project["title"]}</h3><div class="muted">Metode: {project["method"]}</div><ul>' + ''.join(f'<li>{item}</li>' for item in project["description"]) + '</ul></div>', unsafe_allow_html=True)

st.markdown('<div class="section-title">🏆 Pelatihan & Sertifikasi</div>', unsafe_allow_html=True)
for cert in CERTIFICATES:
    st.markdown(f'<div class="card"><div class="muted">{cert["category"]}</div><h3>{cert["title"]}</h3></div>', unsafe_allow_html=True)
    if cert["url"].strip():
        st.link_button("📄 Lihat Sertifikat", cert["url"], use_container_width=True)

st.markdown('<div class="section-title">📞 Kontak Profesional</div>', unsafe_allow_html=True)
st.markdown(f'<div class="card"><h3>Email</h3><div>{PROFILE["email"]}</div></div>', unsafe_allow_html=True)
if PROFILE["whatsapp"].strip():
    st.link_button("💬 Hubungi melalui WhatsApp", PROFILE["whatsapp"])

st.markdown('<div class="footer">E-CV · Digital Kreatif · Resya Sahroni Putri</div>', unsafe_allow_html=True)
