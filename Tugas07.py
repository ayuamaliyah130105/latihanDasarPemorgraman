print ('=============== Program Kalkulator Sederhana ==============')

while (True):
    print('\n=============================')
    print('Menu : ')
    print( '1. Hitung Luas segitiga ')
    print( '2. Hitung Luas Persegi Panjang ')
    print( '3. Tentukan Number Ganjil Genap ')
    print( '4. Quit ')

    print('\n=============================')
    listmenu = input("Masukkan Pilihan : ")

    if listmenu == "1":
        print("Menu -- Hitung Luas Segitiga")
        alas = int(input("\nMasukkan Panjang Alas : "))
        tinggi = int(input("Masukkan Tinggi : "))

        rumus1 = 1/2 * alas * tinggi
        print("\nLuas Segitiga : ", rumus1)
        print("\n==== ==== ===== ====")

    elif listmenu == "2":
        print("Menu -- Hitung Luas Persegi Panjang")
        panjang = int(input("\nMasukkan Panjang : "))
        Lebar = int(input("Masukkan Tinggi : "))

        rumus2 = panjang * Lebar
        print("\nLuas Persegi Panjang : ", rumus2)
        print("\n==== ==== ===== ====")

    elif listmenu == "3":
        print("Menu -- Tentukan Number Ganjir Genap")
        angka = int(input("\nMasukkan Angka : "))

        if (angka % 2 == 0) :
            print("\nAngka", angka, "merupakan angka Genap.")
        else:
            print("\nAngka", angka, "merupakan angka Ganjil.")

        print("\n==== ==== ===== ====")

    else:
        menu = input("\nTerima kasih........")
        print("____ ____ ____ ____ ____")
        break

    




    

