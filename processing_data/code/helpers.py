import re

import pandas as pd

class Helper:
    @staticmethod
    def rapikan_teks(teks: str) -> str:
        if pd.isna(teks):
            return ""
        return re.sub(r"\s+", " ", teks).strip()

    @staticmethod
    def rapikan_daftar(teks: str) -> str:
        if pd.isna(teks):
            return ""
        t = re.sub(r"[\r\n]+", ";", str(teks))
        return t.strip()

    @staticmethod
    def slug(teks: str) -> str:
        if pd.isna(teks):
            return ""
        teks = teks.split(" ")
        return "-".join(teks).lower()

    @staticmethod
    def nama_tanpa_gelar(nama: str) -> str:
        gelar = {
            "Prof.",
            "Dr.",
            "Ir.",
            "S.T.",
            "M.T.",
            "M.Sc.",
            "M.Eng.",
            "M.Kom.",
            "M.Kom",
            "S.Kom",
            "S.Kom.",
            "S.Pd",
            "S.Pd.",
            "S.Si",
            "S.Si.",
            "S.E",
            "S.E.",
            "S.H",
            "S.H.",
            "S.Ars",
            "S.Ars.",
            "M.Ars",
            "M.Ars.",
            "M.Sn",
            "M.Sn.",
        }

        nama = nama.split(",")[0].split(" ")
        nama = [kata for kata in nama if kata not in gelar]
        return " ".join(nama)