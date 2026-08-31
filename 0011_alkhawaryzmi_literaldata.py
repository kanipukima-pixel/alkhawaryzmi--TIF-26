# ALKHAWARYZMI BRILLIANT
# NPM  : 2605060011


#1 variabel dan tipe data
nama='alkhawaryzmi brilliant'
umur= 18
berat=66.5

print(f'NAMA  : {nama}')
print(f'UMUR  : {umur} tahun')
print(f'BERAT : {berat} kg')

#2 mengubah tipe data

angka_string = "123"
angka_float = 45.67
angka_integer = 89

data_1 = int(angka_string)# 1. Konversi angka_string menjadi integer
data_2= int(angka_float)# 2. Konversi angka_float menjadi integer
data_3= float(angka_integer)# 3. Konversi angka_integer menjadi float
data_4 = str(angka_integer)# 4. Konversi angka_integer menjadi string

print(data_1,type(data_1))
print(data_2,type(data_2))
print(data_3,type(data_3))
print(data_4,type(data_4))

#3 input dari user

usia = int(input("Masukkan usia Anda: ")) # input tipe integer
tinggi_badan = float(input("Masukkan tinggi badan Anda (dalam meter): ")) #input tipe float
nama = input("Masukkan nama Anda: ") # input tipe string

print(f"Usia Anda: {usia} tahun")
print(f"Tinggi badan Anda: {tinggi_badan} meter")
print(f"Nama Anda: {nama}")
