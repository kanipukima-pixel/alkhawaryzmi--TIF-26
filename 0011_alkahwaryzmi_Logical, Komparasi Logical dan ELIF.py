#NAMA=ALKHAWARYZMI 
#NPM=2605060011
#ROMBEL=1
#TUGAS=LOGICAL, KOMPARASI LOGICAL DAN ELIF




#1. Buatlah program yang meminta user memasukkan usia seseorang, lalu kategorikan usia
#tersebut berdasarkan kriteria berikut:
#• 0 - 12 tahun: Anak-anak
#• 13 - 17 tahun: Remaja
#• 18 - 59 tahun: Dewasa
#• 60 tahun ke atas: lansia

masukan_usia=int(input('masukan usia = '))


if 0<=masukan_usia <=12 :
    print(f'anak anak tidur besok main lagi')
elif 13<=masukan_usia<=17:
    print(f'remaja tidur besok sekolah pagi')  
elif 18<=masukan_usia<=59:
    print(f'dewasa tidur besok kerja pagi')
elif masukan_usia>=60:
    print(f'lansia tidur besok pagi jalan jalan')  
else :
    print('anomali')        
    

    

            