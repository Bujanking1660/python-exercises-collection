#Latihan Linked List
import os

#Membuat class node
class Node:
    def __init__(self,Info):
        self.Info = Info
        self.Next = None

class LinkedList:
    def __init__(self):
        self.Awal = None

    def Kosong(self):
        kosong = False
        if(self.Awal is None):
            kosong = True
        return kosong
    
    def TampilData(self):
        print('<< -- Tampil Data -->>')
        if(self.Kosong()):
            print('Data Kosong!')
        else:
            Bantu = self.Awal
            while(Bantu != None):
                print(Bantu.Info,end='')
                if(Bantu.Next is not None):
                    print(' ---> ',end='')

                Bantu = Bantu.Next

    def Penghancuran(self):
        Phapus = self.Awal
        while(Phapus is not None): #bisa menggunakan while(not self.Kosong())
            self.Awal = self.Awal.Next
            del(Phapus)
            Phapus = self.Awal
    
    def PenambahanDepan(self,AngkaBaru):
        Baru = Node(AngkaBaru)
        if(self.Kosong()):
            Baru.Next = None
        else:
            Baru.Next = self.Awal
        
        self.Awal = Baru

    def PenambahanBelakang(self,AngkaBaru):
        Baru = Node(AngkaBaru)
        if(self.Kosong()):
            Baru.Next = None
        else:
            Bantu = self.Awal
            while(Bantu.Next is not None):
                Bantu = Bantu.Next
            Bantu.Next = Baru

    def PenambahanTengah(self,AngkaBaru):
        self.TampilData()
        SisipSetelah = int(input("Sisip Setelah Angka : "))
        Ketemu = False
        Bantu = self.Awal

        while(Ketemu is False and Bantu is not None):
            if(Bantu.Info == SisipSetelah):
                Ketemu = True
            else:
                Bantu = Bantu.Next
        
        if(Ketemu):
            if(Bantu.Next == None):
                self.PenambahanBelakang()
            else:
                Baru = Node(AngkaBaru)
                Baru.Next = Bantu.Next
                Bantu.Next = Baru
        else:
            print('Angka tidak ditemukan!')

    def MenuUtama(self,Pilih):
        print('<< MENU UTAMA >>')
        print('1. Penambahan')
        print('2. Pengubahan')
        print('3. Pencarian')
        print('4. Pengurutan')
        print('0. Keluar')
        Pilih = int(input("Pilihan Anda : "))
        while(Pilih <= 0 and Pilih > 5):
            print('Pilihan tidak valid, harap memilih kembali!')
            os.system('pause')
            os.system('cls')
            Pilih = int(input("Pilihan Anda : "))
        return Pilih

    def MenuTambah(self,PilihTambah):
        print('<< MENU TAMBAH >>')
        print('1. Penambahan Depan')
        print('2. Penambahan Belakang')
        print('3. Penambahan Tengah')
        print('0. Keluar')
        PilihTambah = int(input("Pilihan Anda : "))
        while(PilihTambah <= 0 and PilihTambah > 3):
            print('Pilihan tidak valid, harap memilih kembali!')
            os.system('pause')
            os.system('cls')
            PilihTambah = int(input("Pilihan Anda : "))
        return PilihTambah



#Program Utama
List1 = LinkedList()

Pilih = 0
Pilih = List1.MenuUtama(Pilih)

while(Pilih != 0):
    os.system('cls')
    match (Pilih):
        case 1:
            print('Penambahan')
            PilihTambah = 0
            PilihTambah = List1.MenuTambah(PilihTambah)
            while(PilihTambah != 0):
                match (PilihTambah):
                    case 1:
                        os.system('cls')
                        print('Penambahan Di Depan')
                        AngkaBaru = int(input("Masukkan Angka Baru di Depan : "))
                        List1.PenambahanDepan(AngkaBaru)
                        print()
                        List1.TampilData()

                    case 2:
                        os.system('cls')
                        print('Penambahan Di Belakang')
                        AngkaBaru = int(input("Masukkan Angka Baru di Belakang : "))
                        List1.PenambahanBelakang(AngkaBaru)
                        print()
                        List1.TampilData()

                    case 3:
                        os.system('cls')
                        print('Penambahan Di Tengah')
                        AngkaBaru = int(input("Masukkan Angka Baru di Belakang : "))
                        List1.PenambahanTengah(AngkaBaru)
                        print()
                        List1.TampilData()
                print()
                os.system('pause')        
                PilihTambah = List1.MenuTambah(PilihTambah)
            
        case 2:
            print('Pengubahan')
        case 3:
            print('Pengapusan')
        case 4:
            print('Pencarian')
        case 5:
            print('Pengurutan')

    Pilih = List1.MenuUtama(Pilih)

os.system('pause')
List1.Penghancuran()
List1.TampilData()