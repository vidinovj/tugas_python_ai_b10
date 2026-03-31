# tugas3.py - (Tugas Python AI B10)

# 1. Deklarasi Variabel
hero_name = "Pangeran Vidi" # string
level = 10 # integer
health_points = 95.5 # float
is_alive = True # bool
inventory = ["Pedang", "Perisai", "Spell", "Peta", "Kunci"] # list

print("- STATUS KARAKTER RPG -")
print(f"Nama Hero: {hero_name} | Tipe: {type(hero_name)}")
print(f"Level    : {level} | Tipe: {type(level)}")
print(f"HP       : {health_points} | Tipe: {type(health_points)}")
print(f"Hidup    : {is_alive} | Tipe: {type(is_alive)}")
print(f"Tas      : {inventory} | Tipe: {type(inventory)}")
print("-" * 3)

# 2. Manipulasi String
quest_title = "misi penyelamatan princess"
print("\n[INFO QUEST]")
print("Judul Quest (Original):", quest_title)
print("Judul Quest (High):", quest_title.upper())
print("Judul Quest (Secret):", quest_title.lower())
print("Panjang Judul Quest:", len(quest_title), "karakter")
print("Status:", quest_title + " - ongoing")

# 3. Operasi Matematika Sederhana
damage_power = 25
enemy_defense = 7
print("\n BATTLE ")
print(f"Power serangan: {damage_power}, Defense musuh: {enemy_defense}")
print("Total damage (+):", damage_power + 10)
print("Sisa nyawa musuh (-):", 100 - damage_power)
print("Bonus Combo (*):", damage_power * 2)
print("Rata-rata damage (/):", damage_power / 2)
print("Damage true (//):", damage_power // enemy_defense)
print("Sisa tenaga (%):", damage_power % enemy_defense)

# 4. List dan Akses Elemen
print("\n INVENTORY ")
print("Item di slot ke-3:", inventory[2])

inventory.append("Batu Ajaib")
print("Menemukan item baru! Isi tas:", inventory)

inventory.remove("Peta")
print("Membuang 'Peta' agar tas ringan. Isi tas:", inventory)

# 5. Penggunaan Input dari User
print("\n- PENDAFTARAN GUILD PETUALANG -")
nama_pendaftar = input("Siapa namamu, Petualang? ")
umur_pendaftar = input("Berapa usiamu? ")

print(f"\nKARTU ANGGOTA")
print(f"Halo, nama saya {nama_pendaftar} dan umur saya {umur_pendaftar} tahun.")
print("Selamat bergabung di Guild AI B10!")