
#NAMA:ALKHAWARYZMI
#NPM:2605060011
#ROMBEL:1


##1

# List awal
kendaraan = ['motor', 'mobil', 'sepeda', 'bus']

# a. Tambahkan 'truk' di akhir list
kendaraan.append('truk')

# b. Sisipkan 'becak' pada index ke-1
kendaraan.insert(1, 'becak')

# c. Hapus data yang berada paling belakang dari list tersebut
kendaraan.pop()

# d. Ubah elemen 'sepeda' menjadi 'skuter'
# Setelah perubahan a, b, c: 'sepeda' berada pada index 3
index_sepeda = kendaraan.index('sepeda')
kendaraan[index_sepeda] = 'skuter'

# e. Tampilkan informasi jumlah total data di dalam list tersebut
total_data = len(kendaraan)
print("Jumlah total data dalam list:", total_data)
print("Isi list kendaraan saat ini:", kendaraan)


##2

# List awal
angka = [75, 80, 90, 75, 85, 100, 65]

# a. Cari tahu di indeks ke berapa skor 100 berada
indeks_100 = angka.index(100)
print(f"a. Skor 100 berada pada indeks ke-{indeks_100}")

# b. Hitung ada berapa banyak siswa yang mendapatkan skor 75
banyak_75 = angka.count(75)
print(f"b. Jumlah siswa dengan skor 75: {banyak_75}")

# c. Urutkan list skor_ujian dari nilai terkecil hingga terbesar
angka.sort()
print(f"c. List setelah diurutkan (terkecil ke terbesar): {angka}")

# d. Balikkan urutan list (terbesar ke terkecil)
angka.reverse()
# Alternatif: angka.sort(reverse=True)
print(f"d. List setelah dibalik (terbesar ke terkecil): {angka}")

##3

# List awal
Menu_utama = ["Nasi Goreng", "Mie Ayam"]
menu_tambahan = ["Kerupuk", "Es Teh"]

# Menggabungkan menu_tambahan ke dalam Menu_utama menggunakan fungsi extend()
Menu_utama.extend(menu_tambahan)

# Menampilkan hasil data gabungan
print("Menu Gabungan:", Menu_utama)


#4
# Data awal
data_barang = [["Buku", 5000], ["Pensil", 2000], ["Penggaris", 3000]]

# a. Menampilkan harga dari "Pensil" menggunakan indeks baris dan kolom
# "Pensil" berada di baris indeks ke-1, dan harga (2000) berada di kolom indeks ke-1
harga_pensil = data_barang[1][1]
print(f"a. Harga dari Pensil: {harga_pensil}")

# b. Menggunakan perulangan untuk membaca dan menampilkan data sesuai format
print("\nb. Daftar Informasi Barang:")
for nama, harga in data_barang:
    print(f"Nama: {nama}, Harga: {harga}")

