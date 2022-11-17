print ('=============== Menghitung Studi Kasus ==============')

while (True):
    print('\n=============================')
    print('Menu : ')
    print( '1. Menghitung Umur Saat Ini ')
    print( '2. Menghitung Sisa Tahun Cicilan ')
    print( '3. Menghitung BMI Berat Badan ')
    print( '4. Quit ')

    print('\n=============================')
    listmenu = input("Masukkan Pilihan : ")
    
    if listmenu == "1":
        print("Menu -> Menghitung umur saat ini")
        from datetime import datetime, date
        print("\nPerhatikan!")
        print("Format input tanggal lahir wajib 'dd mm yyyy', contoh '01 01 2000' ")
        tanggal_lahir = datetime.strptime(
            input("\nMasukan tanggal lahir anda : "), "%d %m %Y")

        def jul_calculation_age(born):
            today = date.today()
            return today.year - born.year - ((today.month, today.day) < (born.month, born.day))

        umur = jul_calculation_age(tanggal_lahir)

        print("\nUmur anda saat ini adalah :", umur, "Tahun")

        print("=== === === === ===")

    elif listmenu == "2":
        print("Menu -> Menghitung sisa tahun cicilan")

        print("\nBarang-barang Kredit")
        print(" 1. Laptop = Rp.10.000.000,-")
        print(" 2. Motor = Rp.20.000.000,-")
        print(" 3. Mobil = Rp.100.000.000,-")
        print(" 4. Quit")

        print(" \n----------------------------------------")

        listMenu2 = input("Masukan Pilihan : ")

        if listMenu2 == "1":
            print("Menu -> Menghitung sisa tahun cicilan -> Laptop = Rp.10.000.000,-")

            print("\nPerhatian!")
            print("Angsuran perbulan-Nya adalah Rp.833.333,- selama 12 bulan ")

            listMenu3 = input("\nBerapa bulan yang sudah dibayar : ")

            if listMenu3 == "1":
                sisa = 833.333 * 11

                print("\nAngsuran anda masih kurang Rp.", sisa, "untuk 11 bulan")
                print("\n=== === === === ===")

            elif listMenu3 == "2":
                sisa = 833.333 * 10

                print("\nAngsuran anda masih kurang Rp.", sisa, "untuk 10 bulan")
                print("\n=== === === === ===")

            elif listMenu3 == "3":
                sisa = 833.333 * 9

                print("\nAngsuran anda masih kurang Rp.", sisa, "untuk 9 bulan")
                print("\n=== === === === ===")

            elif listMenu3 == "4":
                sisa = 833.333 * 8

                print("\nAngsuran anda masih kurang Rp.", sisa, "untuk 8 bulan")
                print("\n=== === === === ===")

            elif listMenu3 == "5":
                sisa = 833.333 * 7

                print("\nAngsuran anda masih kurang Rp.", sisa, "untuk 7 bulan")
                print("\n=== === === === ===")

            elif listMenu3 == "6":
                sisa = 833.333 * 6

                print("\nAngsuran anda masih kurang Rp.", sisa, "untuk 6 bulan")
                print("\n=== === === === ===")

            elif listMenu3 == "7":
                sisa = 833.333 * 5

                print("\nAngsuran anda masih kurang Rp.", sisa, "untuk 5 bulan")
                print("\n=== === === === ===")

            elif listMenu3 == "8":
                sisa = 833.333 * 4

                print("\nAngsuran anda masih kurang Rp.", sisa, "untuk 4 bulan")
                print("\n=== === === === ===")

            elif listMenu3 == "9":
                sisa = 833.333 * 3

                print("\nAngsuran anda masih kurang Rp.", sisa, "untuk 3 bulan")
                print("\n=== === === === ===")

            elif listMenu3 == "10":
                sisa = 833.333 * 2

                print("\nAngsuran anda masih kurang Rp.", sisa, "untuk 2 bulan")
                print("\n=== === === === ===")

            elif listMenu3 == "11":
                sisa = 833.333 * 1

                print("\nAngsuran anda masih kurang Rp.", sisa, "untuk 1 bulan")
                print("\n=== === === === ===")

            else:
                print("\nMaaf input anda Salah, Terima kasih ... byJulhan")
                print("--- --- --- --- ---")

        elif listMenu2 == "2":
            print("Menu -> Menghitung sisa tahun cicilan -> Motor = Rp.20.000.000,-")

            print("\nPerhatian!")
            print("Angsuran perbulan-Nya adalah Rp.1.666.666,- selama 12 bulan ")

            listMenu3 = input("\nBerapa bulan yang sudah dibayar : ")

            if listMenu3 == "1":
                sisa = 1.666666 * 11

                print("\nAngsuran anda masih kurang Rp.", sisa, "untuk 11 bulan")
                print("\n=== === === === ===")

            elif listMenu3 == "2":
                sisa = 1.666666 * 10

                print("\nAngsuran anda masih kurang Rp.", sisa, "untuk 10 bulan")
                print("\n=== === === === ===")

            elif listMenu3 == "3":
                sisa = 1.666666 * 9

                print("\nAngsuran anda masih kurang Rp.", sisa, "untuk 9 bulan")
                print("\n=== === === === ===")

            elif listMenu3 == "4":
                sisa = 1.666666 * 8

                print("\nAngsuran anda masih kurang Rp.", sisa, "untuk 8 bulan")
                print("\n=== === === === ===")

            elif listMenu3 == "5":
                sisa = 1.666666 * 7

                print("\nAngsuran anda masih kurang Rp.", sisa, "untuk 7 bulan")
                print("\n=== === === === ===")

            elif listMenu3 == "6":
                sisa = 1.666666 * 6

                print("\nAngsuran anda masih kurang Rp.", sisa, "untuk 6 bulan")
                print("\n=== === === === ===")

            elif listMenu3 == "7":
                sisa = 1.666666 * 5

                print("\nAngsuran anda masih kurang Rp.", sisa, "untuk 5 bulan")
                print("\n=== === === === ===")

            elif listMenu3 == "8":
                sisa = 1.666666 * 4

                print("\nAngsuran anda masih kurang Rp.", sisa, "untuk 4 bulan")
                print("\n=== === === === ===")

            elif listMenu3 == "9":
                sisa = 1.666666 * 3

                print("\nAngsuran anda masih kurang Rp.", sisa, "untuk 3 bulan")
                print("\n=== === === === ===")

            elif listMenu3 == "10":
                sisa = 1.666666 * 2

                print("\nAngsuran anda masih kurang Rp.", sisa, "untuk 2 bulan")
                print("\n=== === === === ===")

            elif listMenu3 == "11":
                sisa = 1.666666 * 1

                print("\nAngsuran anda masih kurang Rp.", sisa, "untuk 1 bulan")
                print("\n=== === === === ===")

            else:
                print("\nMaaf input anda Salah, Terima kasih ... byJulhan")
                print("--- --- --- --- ---")

        elif listMenu2 == "3":
            print("Menu -> Menghitung sisa tahun cicilan -> Mobil = Rp.100.000.000,-")

            print("\nPerhatian!")
            print("Angsuran perbulan-Nya adalah Rp.8.333.333,- selama 12 bulan ")

            listMenu3 = input("\nBerapa bulan yang sudah dibayar : ")

            if listMenu3 == "1":
                sisa = 8.333333 * 11

                print("\nAngsuran anda masih kurang Rp.", sisa, "untuk 11 bulan")
                print("\n=== === === === ===")

            elif listMenu3 == "2":
                sisa = 8.333333 * 10

                print("\nAngsuran anda masih kurang Rp.", sisa, "untuk 10 bulan")
                print("\n=== === === === ===")

            elif listMenu3 == "3":
                sisa = 8.333333 * 9

                print("\nAngsuran anda masih kurang Rp.", sisa, "untuk 9 bulan")
                print("\n=== === === === ===")

            elif listMenu3 == "4":
                sisa = 8.333333 * 8

                print("\nAngsuran anda masih kurang Rp.", sisa, "untuk 8 bulan")
                print("\n=== === === === ===")

            elif listMenu3 == "5":
                sisa = 8.333333 * 7

                print("\nAngsuran anda masih kurang Rp.", sisa, "untuk 7 bulan")
                print("\n=== === === === ===")

            elif listMenu3 == "6":
                sisa = 8.333333 * 6

                print("\nAngsuran anda masih kurang Rp.", sisa, "untuk 6 bulan")
                print("\n=== === === === ===")

            elif listMenu3 == "7":
                sisa = 8.333333 * 5

                print("\nAngsuran anda masih kurang Rp.", sisa, "untuk 5 bulan")
                print("\n=== === === === ===")

            elif listMenu3 == "8":
                sisa = 8.333333 * 4

                print("\nAngsuran anda masih kurang Rp.", sisa, "untuk 4 bulan")
                print("\n=== === === === ===")

            elif listMenu3 == "9":
                sisa = 8.333333 * 3

                print("\nAngsuran anda masih kurang Rp.", sisa, "untuk 3 bulan")
                print("\n=== === === === ===")

            elif listMenu3 == "10":
                sisa = 8.333333 * 2

                print("\nAngsuran anda masih kurang Rp.", sisa, "untuk 2 bulan")
                print("\n=== === === === ===")

            elif listMenu3 == "11":
                sisa = 8.333333 * 1

                print("\nAngsuran anda masih kurang Rp.", sisa, "untuk 1 bulan")
                print("\n=== === === === ===")

            else:
                print("\nMaaf inputan anda Salah, Silahkan Ulangi Kembali ... ")
                print("--- --- --- --- ---")

        else:
            print("\nTerima kasih ... ")
            print("--- --- --- --- ---")
            break


    elif listmenu == "3" :
        print("Menu -- Menghitung BMI Berat Badan")
        Berat_Badan = int(input("\nMasukkan Berat Badan Anda (Kg) :"))
        Tinggi_Badan = int(input("\nMasukkan Tinggi Badan Anda (cm):, "))

        rumus2 = Tinggi_Badan / 100
        rumus3 = Berat_Badan / (rumus2*rumus2)
        BMI_Berat_Badan = rumus3    


        if (rumus3 == True):
            BMI_Berat_Badan_int = int(rumus3)
        elif BMI_Berat_Badan< 18.5 :
            Anda = "Berat Badan Anda Kurang"
        elif BMI_Berat_Badan> 18.5 and rumus3 < 24.9:
            Anda = "Berat Badan Anda Normal"
        elif BMI_Berat_Badan> 25 and rumus3 < 29.9:
            Anda = "Anda Kelebihan Berat Badan"
        elif BMI_Berat_Badan > 30 :
            Anda = "Anda Obesitas"
    
            
        print("\nBMI berat badan anda Adalah : ", Anda, )
    
        print("\n==== ==== ===== ====")

    else:
        print("\nTerima kasih ... ")
        print("--- --- --- --- ---")
        break