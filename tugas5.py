# tugas5.py - (Tugas Python AI B10)

# --- FUNCTIONS ---

def greet(nama: str) -> str:
    """Mengembalikan teks sapaan."""
    return f"Halo, {nama}!"

def tambah(a: float, b: float = 0.0) -> float:
    """Mengembalikan hasil penjumlahan a + b."""
    return a + b

def rata_rata(angka: list[float]) -> float:
    """Mengembalikan rata-rata (2 angka di belakang koma)."""
    if not angka:
        return 0.0
    hasil = sum(angka) / len(angka)
    return round(hasil, 2)

# --- CLASS STUDENT ---

class Student:
    def __init__(self, nama: str, nim: str):
        self.nama = nama
        self.nim = nim
        self.nilai = [] # Nilai awal kosong

    def tambah_nilai(self, skor: float):
        """Menambah satu nilai ke list."""
        self.nilai.append(skor)

    def rata_nilai(self) -> float:
        """Menghitung rata-rata nilai menggunakan fungsi rata_rata()."""
        return rata_rata(self.nilai)

    def status(self, threshold: float = 70.0) -> str:
        """Mengecek status kelulusan berdasarkan threshold."""
        if self.rata_nilai() >= threshold:
            return "LULUS"
        else:
            return "TIDAK LULUS"

    def __str__(self) -> str:
        """Representasi string dari objek Student."""
        return (f"Student(nama='{self.nama}', nim='{self.nim}', "
                f"rata={self.rata_nilai()}, status={self.status()})")

# --- DEMO ---

if __name__ == "__main__":
    print("\n=== FUNCTIONS ===")
    print(greet("Arifian"))
    print(f"Tambah(5, 7)  : {tambah(5, 7)}")
    print(f"Tambah(10)     : {tambah(10)}")
    print(f"Rata-rata[80, 90, 100]: {rata_rata([80, 90, 100])}")
    print(f"Rata-rata[]    : {rata_rata([])}")

    print("\n=== CLASS STUDENT ===")
    
    # Mahasiswa 1
    s1 = Student("Budi", "A123")
    s1.tambah_nilai(85.0)
    s1.tambah_nilai(80.0)
    print(s1)
    print(f"Detail -> Rata: {s1.rata_nilai()}, Status: {s1.status()}")

    # Mahasiswa 2
    s2 = Student("Siti", "B456")
    s2.tambah_nilai(60.0)
    s2.tambah_nilai(65.5)
    print(s2)
    print(f"Detail -> Rata: {s2.rata_nilai()}, Status: {s2.status()}")
    print("-" * 20)
