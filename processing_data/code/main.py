import pandas as pd
from helpers import Helper
from config import NAMA_PRODI

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