# tugas6.py - (Tugas Python AI B10)

import numpy as np
import pandas as pd
import os

# Setup seed agar output konsisten
np.random.seed(42)

# 1. NumPy – Data & Statistik
# Membuat array berisi 10 nilai ujian acak antara 50-100
nilai_ujian = np.random.randint(50, 101, size=10)

stats_numpy = {
    "Rata-rata": np.mean(nilai_ujian),
    "Median": np.median(nilai_ujian),
    "Standar Deviasi": round(np.std(nilai_ujian), 2),
    "Nilai Min": np.min(nilai_ujian),
    "Nilai Max": np.max(nilai_ujian)
}

# 2. pandas – DataFrame
data = {
    "nama": ["Arif", "Budi", "Citra", "Dedi", "Eka"],
    "nim": ["A001", "A002", "A003", "A004", "A005"],
    "nilai": nilai_ujian[:5]  # Ambil 5 data pertama dari array NumPy
}

df = pd.DataFrame(data)

# Tambahkan kolom status
df['status'] = df['nilai'].apply(lambda x: "LULUS" if x >= 70 else "TIDAK LULUS")

# 3. OOP Sederhana
class GradeBook:
    def __init__(self, dataframe: pd.DataFrame):
        self.df = dataframe

    def average(self) -> float:
        """Menghitung rata-rata kolom nilai."""
        return round(self.df['nilai'].mean(), 2)

    def pass_rate(self, threshold: float = 70.0) -> float:
        """Menghitung persentase kelulusan."""
        lulus_count = len(self.df[self.df['nilai'] >= threshold])
        return round((lulus_count / len(self.df)) * 100, 2)

    def save_summary(self, path: str):
        """Menulis ringkasan ke file .txt."""
        total_rows = len(self.df)
        lulus = len(self.df[self.df['status'] == "LULUS"])
        tidak_lulus = total_rows - lulus
        
        with open(path, "w") as f:
            f.write("=== RINGKASAN TUGAS 6 ===\n")
            f.write("-" * 25 + "\n")
            f.write("STATISTIK NUMPY (10 Data):\n")
            for k, v in stats_numpy.items():
                f.write(f"{k}: {v}\n")
            
            f.write("\nRINGKASAN DATAFRAME (5 Data):\n")
            f.write(f"Total Baris      : {total_rows}\n")
            f.write(f"Jumlah Lulus     : {lulus}\n")
            f.write(f"Jumlah Tidak Lulus: {tidak_lulus}\n")
            f.write(f"Rata-rata Nilai  : {self.average()}\n")
            f.write(f"Persentase Lulus : {self.pass_rate()}%\n")
            f.write("-" * 25 + "\n")
        print(f"\n[INFO] Ringkasan berhasil disimpan di: {path}")

    def __str__(self):
        return f"GradeBook(Data={len(self.df)}, Rata-rata={self.average()})"

# --- DEMO ---
if __name__ == "__main__":
    print("\n=== NUMPY ===")
    print(f"Data Nilai (10): {nilai_ujian}")
    for k, v in stats_numpy.items():
        print(f"{k}: {v}")

    print("\n=== PANDAS ===")
    print(df.head())

    print("\n=== OOP: GRADEBOOK ===")
    gb = GradeBook(df)
    print(f"Objek GradeBook  : {gb}")
    print(f"Rata-rata Kelas : {gb.average()}")
    print(f"Persentase Lulus: {gb.pass_rate()}%")
    
    # Save Summary
    file_path = "ringkasan_tugas6.txt"
    gb.save_summary(file_path)
