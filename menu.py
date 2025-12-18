# program menu pilihan
# I.S. : pengguna memasukkkna nomor menu
# F.S. : meanampilkan hasil sesuai nomor menu yang dipilih

import os

#badan program
# menampilkan menu
print('MENU PILIHAN')
print('------------')
print('1. Kalkulator sederhana')
print('2. Deret Suku ke-N Deret Fibonacci')
print('3. S = 2/3 - 5/7 + 16/21 - 65/81 + ...')
print('0 KELUAR')

pilih = int(input('Pilihan Anda : '))

#validasi
while(pilih < 0) or (pilih > 3):
    print('nomor menu tidak ada, ulang')
    os.system('pause')
    os.system('cls')

    #ulang
    print('MENU PILIHAN')
    print('------------')
    print('1. Kalkulator sederhana')
    print('2. Deret Suku ke-N Deret Fibonacci')
    print('3. S = 2/3 - 5/7 + 16/21 - 65/81 + ...')
    print('0 KELUAR')

    pilih = int(input('Pilihan Anda : '))

#proses masing masing menu
while(pilih != 0):
    os.system('cls')
    match (pilih):
        case 1:
            print('Kalkulator Sederhana')
            angka1 = int(input('Masukkan nilai ke-1 : '))
            angka2 = int(input('Masukkan nilai ke-2 : '))

            operator = str(input('Masukkan operator tambah(+), kurang(-), kali(x), bagi(:)'))

            if(operator == '+'):
                hasil = angka1 + angka2
            elif(operator == '-'):
                hasil = angka1 - angka2
            elif(operator == 'x'):
                hasil = angka1 * angka2
            elif(operator == ':'):
                hasil = angka1 / angka2
            else:
                print('harap masukkan operator sesuai!')
                
            print(hasil)


        case 2:
            print('Deret Suku ke-N Deret Fibonacci')
        case 3:
            print('S = 2/3 - 5/7 + 16/21 - 65/81 + ...')
        case 0:
            exit()

    os.system('pause')
    os.system('cls')
    print('MENU PILIHAN')
    print('------------')
    print('1. Kalkulator sederhana')
    print('2. Deret Suku ke-N Deret Fibonacci')
    print('3. S = 2/3 - 5/7 + 16/21 - 65/81 + ...')
    print('0 KELUAR')

    pilih = int(input('Pilihan Anda : '))