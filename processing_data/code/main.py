import re
import pandas as pd

from helpers import Helper
from config import NAMA_PRODI

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
def buat_meta_data(row, *, kategori, nama_dosen, sumber_file):
    meta = {"tipe": "profil_dosen", 
            "kategori_dosen": kategori, 
            "nama": nama_dosen,
            "sumber_file": sumber_file}
        
    for profile in ('foto_diri', 'profil_dosen_sinta', 'publikasi_dosen', 'profil_dosen_undip'):
        meta[profile] = row[profile]

    return meta

def buat_dokumen_profil_dosen(df, kategori, sumber_file):
    # 1. Merapikan semua isi di dalam Dataframe
    df = df.map(rapikan_teks)

    # 2. Mengubah nama kolom menjadi seragam
    df = ubah_kolom_standar(kategori, df)

    # 3. Membuat wadah untuk menampung dictionary data bersih
    dokumen = []

    for idx, row in df.itterows():
        # Simpan data nama ke variabel sementara
        nama_dosen = row['nama_dosen'] if row["nama_dosen"] != "" else ""

        # Simpan kategori pengampu atau keahlian ke variabel sementara
        kolom_khusus = row['keahlian'] if row['keahlian'] != "" else ""
        
        baris = [f'''Nama: {nama_dosen}, 
                Nama tanpa gelar: {hapus_gelar(nama_dosen)}, 
                Kategori: Dosen {kategori}''']
        teks = (f"{nama_dosen} adalah dosen {kategori} di Program Studi {NAMA_PRODI}.\n\n"
                + "\n".join(baris))

        # Membuat metadata untuk setiap data
        meta = buat_meta_data(row, 
                              kategori=kategori, 
                              nama_dosen=nama_dosen, 
                              sumber_file=sumber_file)

        # Menggabungkan data ke dokumen
        dokumen.append({"teks": teks, 
                        "meta": meta, 
                        "slug": f"dosen-{kategori}-{buat_slug(hapus_gelar(nama_dosen))}"})

        return dokumen
        
    return

def buat_dokumen_kurikulum():
    return
