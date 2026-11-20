import os



#a luas perseg panjang
def luas_persegipanjang():
    panjang = int(input('masukan panjang '))
    lebar = int(input('masukan lebar '))
    luas= panjang*lebar
    print(f'luas persegi panjang dengan panjang {panjang} dan lebar {lebar} adalah {luas}')
luas_persegipanjang()


#b volume balok
def volume_balok():
    panjang = int(input('masukan panjang '))
    lebar = int(input('masukan lebar '))
    tinggi =int(input('masukan tinggi '))
    volume = panjang*lebar*tinggi
    print(f'luas persegi panjang dengan panjang {panjang} dan lebar {lebar}  dan tinggi {tinggi} adalah {volume}')
volume_balok()


#c luas lingkaran
def luas_lingkaran():
    jari = int(input('masukan jari jari '))
    luas = 3.14*jari**2
    print(f'luas lingkaran dengan jari jari {jari}  adalah {luas}')
luas_lingkaran()




#d volume bola
def volume_bola():    
    jari = int(input('masukan jari jari '))
    volume =  3.14*jari**3*(4/3)
    print(f'volume bola dengan jari jari {jari}  adalah {volume}')        
volume_bola()    
    

    