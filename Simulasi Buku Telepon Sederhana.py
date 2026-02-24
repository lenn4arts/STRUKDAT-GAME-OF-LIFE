# Simulasi Buku Telepon Sederhana
# Menggunakan struktur data List dan Dictionary

buku_telepon = []

def tampilkan_kontak():
    if not buku_telepon:
        print("\nBuku telepon kosong.\n")
        return
    
    print("\n=== Daftar Kontak ===")
    for i, kontak in enumerate(buku_telepon, start=1):
        print(f"{i}. Nama  : {kontak['nama']}")
        print(f"   Nomor : {kontak['nomor']}")
        print("------------------------")
    print()

def tambah_kontak():
    nama = input("Masukkan Nama  : ")
    nomor = input("Masukkan Nomor : ")
    
    buku_telepon.append({
        "nama": nama,
        "nomor": nomor
    })
    
    print("Kontak berhasil ditambahkan!\n")

def cari_kontak():
    keyword = input("Masukkan nama yang dicari: ").lower()
    ditemukan = False
    
    for kontak in buku_telepon:
        if keyword in kontak["nama"].lower():
            print("\nKontak ditemukan:")
            print(f"Nama  : {kontak['nama']}")
            print(f"Nomor : {kontak['nomor']}\n")
            ditemukan = True
    
    if not ditemukan:
        print("Kontak tidak ditemukan.\n")

def hapus_kontak():
    tampilkan_kontak()
    if not buku_telepon:
        return
    
    try:
        nomor = int(input("Masukkan nomor urut kontak yang akan dihapus: "))
        if 1 <= nomor <= len(buku_telepon):
            buku_telepon.pop(nomor - 1)
            print("Kontak berhasil dihapus!\n")
        else:
            print("Nomor tidak valid.\n")
    except ValueError:
        print("Input harus berupa angka.\n")

def menu():
    while True:
        print("=== MENU BUKU TELEPON ===")
        print("1. Tampilkan Kontak")
        print("2. Tambah Kontak")
        print("3. Cari Kontak")
        print("4. Hapus Kontak")
        print("5. Keluar")
        
        pilihan = input("Pilih menu (1-5): ")
        
        if pilihan == "1":
            tampilkan_kontak()
        elif pilihan == "2":
            tambah_kontak()
        elif pilihan == "3":
            cari_kontak()
        elif pilihan == "4":
            hapus_kontak()
        elif pilihan == "5":
            print("Terima kasih telah menggunakan Buku Telepon.")
            break
        else:
            print("Pilihan tidak valid.\n")

# Menjalankan program
menu()