from msilib.schema import Condition


print('================================================================')
print('========================== Nilai Kelulusan =====================')
print('================================================================')
while(True):
    Nama    = input("Masukkan Nama Anda : ")
    Jurusan = input("Masukkan Jurusan Anda: ")
    Nilai   = input("Inputkan Nilai Kelulusan: ")

    if (Nilai.isnumeric() == True):
        Nilai_int = int(Nilai)
        if Nilai_int>= 90 :
            grade    = "A"
            Predikat = "Dengan Pujian"
        elif Nilai_int>= 80:
            grade = "B"
            Predikat = "Sangat Memuaskan"
        elif Nilai_int>= 70:
            grade = "C"
            Predikat = "Memuaskan"
        elif Nilai_int>= 60:
            grade = "D"
            Predikat = "Tidak Memuaskan"
        elif Nilai_int>= 0:
            grade = "E"
            Predikat = "Tidak LULUS"
        
        print('================================================================')
        print('========================== Nilai Kelulusan =====================')
        print('================================================================')
        print("grade Anda    : ", grade)
        print("predikat Anda : ", Predikat)
        print('Tetap Semangat dan Terus Berusaha ya!')
    else :
        print('================================================================')
        print('========================== Nilai Kelulusan =====================')
        print('================================================================')
        print('Grade Tidak Terbaca, Coba Lagi!')
        
    print('================================================================')
        
        
    apakahLanjut = input('apakah ingin kembali? "Y" lanjut "N" Tidak : ')
    if (apakahLanjut != 'Y' ) :
        break


