# tugas4.py - (Tugas Python AI B10)

# 1. List - akses & manipulasi
tas_barang = ["Pedang", 10, "Ramuan", 75.5, "Kunci", "Peta", 100] # ≥ 6 elemen campuran

print("\n INVENTORY ")
print(f"Isi Tas Awal: {tas_barang}")
print(f"Elemen Pertama: {tas_barang[0]}, Terakhir: {tas_barang[-1]}")
print(f"Slicing [1:6:2]: {tas_barang[1:6:2]}")

print("\n[UPDATE TAS]")
tas_barang.append("Obor")
tas_barang.insert(2, "Perisai")
tas_barang.extend(["Koin", 5])
print(f"Sesudah ditambah: {tas_barang}")

tas_barang.pop()
if 75.5 in tas_barang:
    tas_barang.remove(75.5)
print(f"Sesudah dihapus: {tas_barang}")

# 2. Tuple – immutability & unpacking
koordinat_desa = ("Desa Sukamaju", 125, 450, "Z-Zone", "Level 1")

print("\n[LOKASI PETUALANG]")
print(f"Data Lokasi: {koordinat_desa}")
print(f"Panjang: {len(koordinat_desa)}, Indeks ke-0: {koordinat_desa[0]}")

nama_desa, x, y, *info_tambahan = koordinat_desa
print(f"Unpacking -> Nama: {nama_desa}, Koordinat: ({x},{y}), Sisa: {info_tambahan}")

# 3. Set – keunikan & operasi himpunan
skill_api = {"Fireball", "Burn", "Heat", "Smoke"}
skill_air = {"Water", "Ice", "Steam", "Heat"}

print("\n SKILL MAGIC ")
print(f"Skill Api: {skill_api}")
print(f"Skill Air: {skill_air}")
print(f"Union (|): {skill_api | skill_air}")
print(f"Intersection (&): {skill_api & skill_air}")
print(f"Difference (-): {skill_api - skill_air}")
print(f"Symmetric Difference (^): {skill_api ^ skill_air}")

cek_set = {1, 2, 2, 3, 3, 3}
print(f"Cek Duplikat { {1, 2, 2, 3, 3, 3} }: {cek_set}")

# 4. Dictionary – key/value dasar
data_player = {
    "nama": "Vadin",
    "nim": "B10-001",
    "angkatan": 2026,
    "kota": "Bandung"
}

print("\n- PROFIL PETUALANG -")
data_player["level"] = 99
data_player["kota"] = "Jakarta"
if "nim" in data_player:
    del data_player["nim"]

print(f"Data Sekarang: {data_player}")
print(f"Keys: {list(data_player.keys())}")
print(f"Values: {list(data_player.values())}")
print(f"Items: {list(data_player.items())}")

print("\nIterasi Key: Value")
for key, val in data_player.items():
    print(f"- {key}: {val}")

# 5. Nested structures
daftar_quest = [
    {"judul": "Lawan Naga", "penulis": "Raja", "tahun": 2024},
    {"judul": "Cari Harta", "penulis": "Peta Tua", "tahun": 2025},
    {"judul": "Masak Air", "penulis": "Ibu Kantin", "tahun": 2023},
    {"judul": "Coding Python", "penulis": "Gemini", "tahun": 2026}
]

print("\n[DAFTAR QUEST]")
print("Semua Judul Quest:")
for q in daftar_quest:
    print(f"- {q['judul']}")

quest_baru = [q['judul'] for q in daftar_quest if q['tahun'] >= 2025]
print(f"Quest terbaru (>= 2025): {quest_baru}")

# 6. Comprehension & utilitas
print("\n- COMPREHENSION -")
genap = [i for i in range(1, 21) if i % 2 == 0]
kuadrat = [i**2 for i in range(1, 21)]
print(f"List Genap (1-20): {genap}")
print(f"List Kuadrat (1-20): {kuadrat}")

tipe_angka = {i: "genap" if i % 2 == 0 else "ganjil" for i in range(1, 11)}
print(f"Dict Tipe Angka (1-10): {tipe_angka}")

kalimat = "belajar python seru banget"
huruf_unik = {h.lower() for h in kalimat if h.isalpha()}
print(f"Huruf unik (lowercase): {huruf_unik}")

# 7. Keanggotaan & pencarian sederhana
print("\n PENCARIAN ")
search_item = "Pedang"
if search_item in tas_barang:
    posisi = tas_barang.index(search_item)
    print(f"Item '{search_item}' ketemu di indeks: {posisi}")
else:
    print(f"Item '{search_item}' nggak ada.")

print(f"Apakah 'Ice' ada di skill api? {'Ice' in skill_api}")
