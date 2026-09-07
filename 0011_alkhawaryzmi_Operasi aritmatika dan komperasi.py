#NAMA = ALKHAWARYZMI BRILLIANT
#NPM = 2605060011
#TUGAS = ARITMATKA DAN KOMPERASI

panjang=12
lebar=5
tinggi=8
#luas
luas_samping2=panjang*tinggi
luas_samping1=lebar*tinggi
luas_alas1= panjang * lebar
#luas permukaan
luas_permukaan= 2 * (luas_alas1 + luas_samping1 + luas_samping2)
#volume
volume= panjang * lebar * tinggi
#keliling
keliling_alas1= 2 * (panjang + lebar)
keliling_samping2= 2 * (panjang + tinggi)
keliling_samping1= 2 * (lebar + tinggi)
keliling_rusuk= 4 * (panjang + lebar + tinggi)
#output luas
print('luas alas 1 bangunan:', luas_alas1)
print('luas samping 1 bangunan:', luas_samping1)
print('luas samping 2 bangunan:', luas_samping2)
print("Luas alas bangunan:", luas_alas1)
print("Luas permukaan bangunan:", luas_permukaan)
print('\n')
#output volume
print("Volume bangunan:", volume)
print('\n')
#output keliling
print("Keliling alas 1 bangunan:", keliling_alas1)
print("Keliling samping 1 bangunan:", keliling_samping1)
print("Keliling samping 2 bangunan:", keliling_samping2)
print("Keliling rusuk bangunan:", keliling_rusuk)
print('\n')

#cek luas
cek_luas_alas1= luas_alas1 > 50
cek_luas_samping1= luas_samping1 > 50
cek_luas_samping2= luas_samping2 > 50
cek_luas_permukaan= luas_permukaan > 50

#cek volume
cek_volume= volume == 480


print(f"Volume bangunan bernilai 480, {cek_volume}:")
    
print(f"Luas alas bangunan lebih besar dari 50, {cek_luas_alas1}:")

print(f"Luas samping 1 bangunan lebih besar dari 50, {cek_luas_samping1}:")    
    
print(f"Luas samping 2 bangunan lebih besar dari 50, {cek_luas_samping2}:")    
    
print(f"Luas permukaan bangunan lebih besar dari 50, {cek_luas_permukaan}:")        