# Deskriptif
# membuat variabel nama barang
# membuat variabel harga barang
# membuat variabel persen harga
# input nama barang
# input harga barang
# menghitung harga barang 
# harga barang * persen  / 100
# harga barang
from ast import Break


while(True): 
    nama_barang=input('Masukkan nama barang ')
    harga_barang=input('Masukkan harga barang ')
    persen=15
    harga_keuntungan =int(harga_barang)*persen/100
    harga_jual =int(harga_barang) + harga_keuntungan
    print(nama_barang,'dijual dengan: ',harga_jual)
    
    apakahLanjut = input('apakah ingin lanjut? Y lanjut N tidak')
    if(apakahLanjut != 'Y'):
        break
