import re
import pandas as pd

from helpers import Helper
from config import NAMA_PRODI

<<<<<<< Updated upstream
def dokumen_dosen_dalam(df, kategori, sumber_file):
    dokumen = []

    for idx, row in df.itterows():
        if row['nama_dosen_dalam_tekkom'] == "":
            raise ValueError(f"{sumber_file} : nama kosong di baris excel {idx + 2}")
        nama_tanpa_gelar = Helper.nama_tanpa_gelar(row['nama_dosen_dalam_tekkom'])
        keahlian = row.get("keahlian", "")

        baris = [f"Nama: {row['nama_dosen_dalam_tekkom']}", 
                 f"Nama tanpa gelar: {nama_tanpa_gelar}", 
                 f"Kategori: Dosen {kategori}",
                 f"Bidang keahlian {keahlian}"]
        
        teks = (f"{row['nama_dosen_dalam_tekkom']} adalah dosen {kategori} di Program Studi {NAMA_PRODI}.\n\n"
                    + "\n".join(baris))
        
        meta = {"tipe": "profil_dosen", 
                "kategori_dosen": kategori, 
                "nama": row["nama_dosen_dalam_tekkom"],
                "sumber_file": sumber_file}
        
        for profile in ['foto_profil', 'profil_sinta', 'publikasi', 'profil_undip']:
            meta[profile] = row[profile]
    
        dokumen.append({"teks": teks, 
                        "meta": meta, 
                        "slug": f"dosen-{kategori}-{Helper.slug(nama_tanpa_gelar)}"})
=======
def hapus_gelar(nama: str) -> str:
    gelar = {'Prof.', 'Dr.', 'Ir.', 'S.T.', 
             'M.T.', 'M.Sc.', 'M.Eng.', 'M.Kom.', 
             'S.Kom', 'S.Si', 'S.Si.', 'S.H', 'S.H.', 
             'Eng.', 'Dr.Eng.', 'Dra.', 'Drs.'}
    
    if (nama == ""):
        raise ValueError("Nama tidak boleh kosong")
    
    sampel = nama.split(',')[0].split()
    sampel = [nama for nama in sampel if nama not in gelar]
    return ' '.join(sampel)

def buat_slug(nama: str) -> str:
    if (nama == ""):
        raise ValueError("Nama tidak boleh kosong")
    
    slug = nama.lower().split(' ')
    return '-'.join(slug)

def ubah_kolom_standar(kategori: str, df: pd.DataFrame) -> pd.DataFrame:
    kolom_khusus = 'keahlian' if kategori == 'dalam' else 'pengampu'
    df.columns = ['nama_dosen', kolom_khusus, 'foto_profil', 'profil_sinta', 'publikasi', 'profil_google_scholar']
    return df

def rapikan_teks(teks: str) -> str:
        if pd.isna(teks):
            return ""
        return re.sub(r"\s+", " ", teks).strip()

# ======== DOKUMEN ==========
def buat_dokumen_profil_dosen(df, kategori):
    # 1. Merapikan semua isi di dalam Dataframe
    df = df.map(rapikan_teks)

    # 2. 
    return

def buat_dokumen_kurikulum():
    return
>>>>>>> Stashed changes
