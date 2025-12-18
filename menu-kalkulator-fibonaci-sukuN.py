#Program Menu Pilihan
#I.S.: pengguna memasukkan nomor menu
#F.S.: menampilkan hasil sesuai nomor menu yang dipilih
import os
#badan program

#mengekelompokkan program
def pause():
    os.system('pause')

def cls():
    os.system('cls')

#menu pilihan
def menu():
    print('======================================')
    print('<<<<<< ----- MENU PILIHAN ----- >>>>>>')
    print('======================================')
    print('(1) Kalkulator Sederhana')
    print('(2) Suku Ke-N Dari Deret Fibonacci')
    print('(3) S = 2/3 - 5/7 + 16/21 - 65/81 + ..')
    print('(0) Keluar Program')

#menu kalkulator sederhana
def detail():
    print('==============================================================')
    print('<<<<<<<<<<<<< ------ KALKULATOR SEDERHANA ------ >>>>>>>>>>>>>')
    print('==============================================================')
    print('(1) Penjumlahan ( + )')
    print('(2) Pengurangan ( - )')
    print('(3) Perkalian   ( x )')
    print('(4) Pembagian   ( : )')
    print('(0) Keluar Program')

def kalkulator():
    

    detail()
    #menentukkan jumlah angka yang ingin dioperasikan
    jumlahAngka = int(input("Masukkan jumlah angka yang ingin dioperasikan (minimal 2): ")) 
    while jumlahAngka < 2:
        print("Jumlah angka minimal adalah 2. Silakan coba lagi!")
        jumlahAngka = int(input("Masukkan jumlah angka yang ingin dioperasikan (minimal 2): "))

    #memasukkan angka pertama
    while True:
        try:
            hasil = float(input("Masukkan angka pertama: "))
            break
        except ValueError:
            print("Masukkan angka yang valid.")
            pause()
            cls()
            detail()

    #memasukkan operasi dan angka berikutnya
    for i in range(1, jumlahAngka):
        #mengecek tipe data pada operator
        print(hasil)
        operator = input("Masukkan operator (+, -, x, :): ")
        while operator not in ['+', '-', 'x', ':']:
            print("Operator tidak sesuai dengan menu! Ulangi tekan enter... ")
            pause()
            cls()
            detail()
            print(hasil)
            operator = input("Masukkan operator (+, -, x, :): ")
        print(hasil,operator)

        #mengecek tipe data pada angka selanjutnya
        while True:
            try:
                angkaSelanjutnya = float(input(f"Masukkan angka ke-{i + 1}: "))
                print(hasil,operator,angkaSelanjutnya)
                if operator == '/' and angkaSelanjutnya == 0:
                    print("Pembagian dengan nol tidak diperbolehkan! Ulangi tekan enter... ")
                    pause()
                    cls()
                    print(hasil,operator)
                    continue
                break
            except ValueError:
                print("Masukkan angka yang valid.")
                pause()
                cls()
                detail()
                print(hasil,operator)

        #menghitung angka pertama atau hasil sementara dengan angka selanjutnya
        if operator == '+':
            hasil += angkaSelanjutnya
        elif operator == '-':
            hasil -= angkaSelanjutnya
        elif operator == 'x':
            hasil *= angkaSelanjutnya
        elif operator == ':':
            hasil /= angkaSelanjutnya

    #menampilkan hasil akhir
    print(f"Hasil akhir: {hasil}")
        
def fibonacci():
    print('=================================================')
    print('<<< ----- SUKU KE-N dari DERET FIBONACCI ---- >>>')
    print('=================================================')

    # Validasi input menggunakan while
    while True:
        SukuN = int(input('Masukkan Suku ke-N (1-8) : '))
        if SukuN < 1 or SukuN > 8:
            print('Angka tidak boleh kurang dari 1 dan lebih dari 8. Silakan coba lagi.')
        else:
            break

    AngkaPertama = 0
    AngkaKedua   = 1
    
    for a in range(2, SukuN + 1):
        AngkaKetiga = AngkaPertama + AngkaKedua
        AngkaPertama = AngkaKedua
        AngkaKedua = AngkaKetiga
    print('Suku ke ',a,'adalah',AngkaKedua)
            
#program menghitung Suku S
def SukuS():
    print('=================================================')
    print('<<< HITUNG S = 2/3 - 5/7 + 16/21 - 65/81 + .. >>>')
    print('=================================================')
            
    # memasukkan banyak suku ke-n
    N = int(input("Masukkan suku ke-n : "));

    # validasi banyak suku
    while (N < 1) or (N > 15):
        print(f"Banyak suku harus antara 1 sampai 15! Ulangi tekan enter... ");
        os.system("pause");
        os.system("cls");
        # memasukkan banyak suku ke-n
        N = int(input("Masukkan suku ke-n : "));
                    
    # menghitung S
    S = 0;
    Pembilang = 0;
    Penyebut = 0;
    print("S = ", end="");
    for i in range(N):
        i = i + 1
        Temp = Pembilang;
        if(i == 1): 
            Pembilang = 2 * (i * 1);
            Penyebut = Pembilang + i;
        else :
            Pembilang = (Temp * i) + 1;
            Penyebut = Pembilang + Temp;
        if (i % 2 == 1):
            if (i == 1):
                print(f"{Pembilang:0.0f}/{Penyebut:0.0f}", end="");
            else:
                print(f" + {Pembilang:0.0f}/{Penyebut:0.0f}", end="");
            S = S + Pembilang/Penyebut;
        else:
            print(f" - {Pembilang:0.0f}/{Penyebut:0.0f}", end="");
            S = S - Pembilang/Penyebut;

    # menampilkan nilai S
    print();
    print(f"S = {S:0.3f}");

    

#menampilkan menu
menu() 

#memilih menu
Pilih = int(input('Pilihan Anda? '))

#validasi menu
while(Pilih < 0) or (Pilih > 3):
    print('Harap Pilih Menu 0-3')
    pause()
    cls()
    Pilih = int(input('Pilihan Anda? '))    


#proses masing-masing menu
while (Pilih != 0):
    cls()
    match (Pilih):
        case 1 :
            kalkulator()

        case 2 :
            fibonacci()
            
            
            

            
        
        case 3 :
            SukuS()

    pause()
    cls()
    #menampilkan menu pilihan
    print('======================================')
    print('<<<<<< ----- MENU PILIHAN ----- >>>>>>')
    print('======================================')
    print('(1) Kalkulator Sederhana')
    print('(2) Suku Ke-N Daari Deret Fibonacci')
    print('(3) S = 2/3 - 5/7 + 16/21 - 65/81 + ..')
    print('(0) Keluar Program')
    Pilih = int(input('Pilihan Anda? '))