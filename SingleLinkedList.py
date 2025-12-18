#Program Single Linked List
#I.S : Diberikan harga awal terhadap pointer kepala (Awal)
#F.S : Menampilkan isi linked list

import os

#Pendefinisian linked list
#1. Membuat class untuk simpul/node
class Node:
    def __init__(self,Info):
        self.Info = Info
        self.Next = None

#2. Membuat class untuk linked list
class SingleLinkedList:
    def __init__(self):
        self.Awal = None
    #method memeriksa list kosong atau tidak 
    def Kosong(self):
        kosong = False
        if(self.Awal is None):
            kosong = True

        return kosong #bisa menggunakan return self.Awal is None

    #Method menampilkan isi list
    def TampilData(self):
        print(' -- Isi Linked List -- ')
        if(self.Kosong()):
            print('List kosong')
        else:
            Bantu = self.Awal
            while(Bantu is not None): #bisa menggunakan while(Bantu != None):
                print(Bantu.Info,end='')
                if(Bantu.Next is not None):
                    print(' ---> ',end='')

                Bantu = Bantu.Next
        print()

    #Method menghapus
    def Penghancuran(self):
        Phapus = self.Awal
        while(Phapus is not None): #bisa menggunakan while(not self.Kosong())
            self.Awal = self.Awal.Next
            del(Phapus)
            Phapus = self.Awal

    #Method menampilkan menu penambahan data
    def MenuTambah(self,Menu):
        os.system('cls')
        print(' -- Menu Tambah Data -- ')
        print('1) Tambah Data di Depan')
        print('2) Tambah Data di Belakang')
        print('3) Tambah Data di Tengah')
        print('0) Keluar Menu Tambah Data')
        Menu = int(input('Pilihan Anda :'))
        #VALIDASI  
        return Menu

    #Method penambahan data di awal
    def SisipDepanSingle(self,AngkaBaru):
        Baru = Node(AngkaBaru)
        if(self.Kosong()):
            Baru.Next = None
        else:
            Baru.Next = self.Awal
        self.Awal = Baru

    #Method penambahan data di belakang
    def SisipBelakangSingle(self,AngkaBaru):
        Baru = Node(AngkaBaru)
        if(self.Kosong()):
            self.Awal = Baru
        else:  
            Bantu = self.Awal
            while(Bantu.Next is not None):
                Bantu = Bantu.Next
            Bantu.Next = Baru
            

    #Method penambahan data di tengah
    def SisipTengahSingle(self,AngkaBaru):
        SisipSetelah = int(input('Sisip setelah : '))
        Bantu = self.Awal
        Ketemu = False

        print('Angka ',AngkaBaru,' akan disisipkan setalah angka',SisipSetelah)
        while(not Ketemu) and (Bantu is not None):
            if(Bantu.Info) == SisipSetelah:
                Ketemu = True
            else:
                Bantu = Bantu.Next

        if(Ketemu):
            if(Bantu.Next is None):
                self.SisipBelakangSingle(AngkaBaru)
            else:
                Baru = Node(AngkaBaru)
                Baru.Next = Bantu.Next
                Bantu.Next = Baru
        else:
            print('Angka',SisipSetelah,'tidak ditemukan!')
            


#Badan program utama
#Inisialisasi linked list
List1 = SingleLinkedList()

#Membuat 2 buah simpul (Node1 dan Node2)
Node1 = Node(5) # alloc(Node1) dan Node1^.Info <- 5
Node2 = Node(6)

#Menyambungkan 2 simpul
Node2.Next = None # Memberi nilai nil pada ujung list
Node1.Next = Node2

#Menjadikan linked list
List1.Awal = Node1

#Memanggil method menampilkan isi list
os.system('cls')
List1.TampilData()
os.system('pause')
print()

#Membuat satu simpul kembali dan medan data diisi angka 99 di akhir
Node1 = Node(99)
Node1.Next = None
Node2.Next = Node1

os.system('cls')
List1.TampilData()
os.system('pause')
print()

#Membuat simpul kembali dan medan data diisi angka 100 di awal
Node2 = Node(100)
Node2.Next = List1.Awal
List1.Awal = Node2

os.system('cls')
List1.TampilData()
os.system('pause')
print()

#Menu
Menu = 0
Menu = List1.MenuTambah(Menu)

while(Menu != 0):
    os.system('cls')
    match (Menu):
        case 1:
            print(' -- Penambahan Data di Depan -- ')
            AngkaBaru = int(input('Masukkan sebuah angka baru : '))
            List1.SisipDepanSingle(AngkaBaru)
            print()
            List1.TampilData()
        case 2:
            print(' -- Penambahan Data di Belakang -- ')
            AngkaBaru = int(input('Masukkan sebuah angka baru : '))
            List1.SisipBelakangSingle(AngkaBaru)
            print()
            List1.TampilData()
        case 3:
            print(' -- Penambahan Data di Tengah -- ')
            if(List1.Kosong()):
                print('List masih kosong!')
            else:
                AngkaBaru = int(input('Masukkan sebuah angka baru : '))
                List1.SisipTengahSingle(AngkaBaru)
                print()
                List1.TampilData()

    print()
    os.system('pause')        
    Menu = List1.MenuTambah(Menu)

#Memanggil method penghancuran
List1.Penghancuran()
print()
os.system('cls')
List1.TampilData()