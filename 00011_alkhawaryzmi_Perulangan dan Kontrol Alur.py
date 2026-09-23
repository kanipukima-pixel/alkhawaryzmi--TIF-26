#NAMA=ALKHAWARYZMI BRILLANT
#NPM=2605060011
#KELAS=ROMBEL1





#1. Buat program yang menampilkan bilangan ganjil dan genap dari 1 sampai 50 menggunakan
#perulangan!
#2. Buat program yang menampilkan semua bilangan prima antara 1 sampai 100 menggunakan
#perulangan!

#bIlangan ganjl genap 1-50
print('PROGRAMBLANGAN GANJIL DAN GENAP')
for i in range(1,51):
    if i%2==0:
        print(f'{i} adalah bilangan genap')
    else:
        print(f'{i} adalah bilangan ganjil') 
        
print('\n')        

print('PROGRAM BILANGAN PRIMA 1-100')        
#bIlangan prima 1-100       
for angka in range(2, 101):
    prima = True
    for pembagi in range(2, angka):
        if angka % pembagi == 0:
            prima = False
            break
    if prima == True:
        print(angka)        
    