# 1 Tuple
# a.
mahasiswa=('alkhawaryzmi','2605060011','teknologi informasi')
# b
print(mahasiswa[2])
#c
print(mahasiswa[2] = "Teknologi Informasi") #akan error karena tuple bersifat immutable
#d
nilai_angka=(10, 4, 3, 2, 4, 10, 7, 5)
print(nilai_angka)

#2 set
data_mahasiswa = {
    "nim": "240101",
    "nama": "Budi Santoso",
    "prodi": "Teknologi Informasi"
}
data_mahasiswa['prodi']= 'sastra mesin'
data_mahasiswa['angkatan']= 2026
del data_mahasiswa['nim']
print(data_mahasiswa)

#3
harga_buah={
    "apel": 5000,
    "pisang": 3000,
    "jeruk": 7000,
    "anggur": 15000
}
harga= harga_buah.values()
total =0
for buah, harga in harga_buah.items():
    print(f'harga {buah}: Rp{harga}')
    total += harga
print(f'Total harga buah: Rp{total}')