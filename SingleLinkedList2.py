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

    #Method menampilkan menu utama
    def MenuUtama(self,Utama):
        os.system('cls')
        print(' -- Menu Utama -- ')
        print('1) Tambah Data')
        print('2) Ubah Data')
        print('3) Hapus Data')
        print('4) Cari Simpul')
        print('5) Urut Data')
        print('0) Keluar Menu Utama')
        Utama = int(input('Pilihan Anda :'))
        #VALIDASI  
        return Utama

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
    
    #Method menampilkan menu penghapusan data
    def MenuPenghapusan(self,PilihHapus):
        os.system('cls')
        print(' -- Menu Tambah Data -- ')
        print('1) Hapus Data di Depan')
        print('2) Hapus Data di Belakang')
        print('3) Hapus Data di Tengah')
        print('0) Keluar Menu Tambah Data')
        PilihHapus = int(input('Pilihan Anda :'))
        #VALIDASI  
        return PilihHapus

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
            
    #Method pengubahan data
    def UbahData(self,AngkaBaru):
        if(self.Kosong()):
            print('Data Kosong')
        else:
            AngkaUbah = int(input("Masukkan Data Yang Akan Ubah : "))
            Bantu = self.Awal
            Ketemu = False

            while(not Ketemu) and (Bantu is not None):
                if(Bantu.Info == AngkaUbah):
                    Ketemu = True
                else:
                    Bantu = Bantu.Next

            if(Ketemu):
                Bantu.Info = AngkaBaru
            else:
                print('Data ',AngkaUbah,' yang akan diubah tidak ditemukan!')

    #Method memeriksa list memiliki satu simpul atau lebih
    def SatuNode(self):
        satunode = False
        if(self.Awal.Next == None):
            satunode = True
        return satunode

    #Method penghapusan data di depan
    def HapusDepanSingle(self):
        if(self.Kosong()):
            print('Data Masih Kosong')
        else:
            Phapus = self.Awal
            if(self.SatuNode()):
                self.Awal = None
            else:
                self.Awal = Phapus.Next

            AngkaHapus = Phapus.Info
            del(Phapus)
            os.system('cls')
            print('Angka yang sudah dihapus adalah Angka ',AngkaHapus)

    def HapusBelakangSingle(self):
        if(self.Kosong()):
            print('Data Masih Kosong')
        else:
            Phapus = self.Awal
            if(self.SatuNode()):
                self.Awal = None
            else:
                while(Phapus.Next != None):
                    Phapus = Phapus.Next

                Bantu = self.Awal
                while(Bantu.Next != Phapus):
                    Bantu.Next = None

            AngkaHapus = Phapus.Info
            del(Phapus)
            os.system('cls')
            print('Angka yang sudah dihapus adalah Angka ',AngkaHapus)

    #Method penghapusan data ditengah
    def HapusTengahSingle(self):
        if(self.Kosong()):
            print('Data Masih Kosong')
        else:
            HapusAngka = int(input('Masukkan data yang akan dihapus : '))
            Phapus = self.Awal
            Ketemu = False
            while(not Ketemu) and (Phapus is not None):
                if(Phapus.Info == HapusAngka):
                    Ketemu = True
                else:
                    Phapus = Phapus.Next
            if(Ketemu):
                if(Phapus == self.Awal):
                    self.HapusDepanSingle()
                else:
                    if(Phapus.Next == None):
                        self.HapusBelakangSingle()
                    else:
                        AngkaHapus = Phapus.Info
                        Bantu = self.Awal
                        while(Bantu.Next != Phapus):
                            Bantu = Bantu.Next

                        Bantu.Next = Phapus.Next
                        del(Phapus)
                        os.system('cls')
                        print('Angka yang sudah dihapus adalah Angka ',AngkaHapus)
            else:
                print('Data ',HapusAngka,' yang akan dihapus tidak ada')


    #Method pencarian pointer
    def PecarianNode(self):
        if(self.Kosong()):
            print('Data Masih Kosong')
        else:
            CariNode = int(input('Cari Node :'))
            Bantu = self.Awal
            Posisi = 1
            Ketemu = False
            while(not Ketemu)and(Bantu is not None):
                if(Posisi == CariNode):
                    Ketemu= True
                else:
                    Bantu = Bantu.Next
                    Posisi+=1
            if(Ketemu):
                print('Data ',CariNode,' ditemukan')
            else:
                print('Data ',CariNode,' tidak ditemukan')

    # def Pencarian(self):
    #     if(self.Kosong()):
    #         print('Data Masih Kosong')
    #     else:
    #         CariAngka = int(input('Cari Data : '))
    #         Bantu = List1.Awal
    #         Ketemu = False
    #         while(not Ketemu) and (Bantu != None):
    #             if(Bantu.Info == CariAngka):
    #                 Ketemu = True
    #             else:
    #                 Bantu = Bantu.Next
    #         if(Ketemu):
    #             print('Data ',CariAngka,' ditemukan')
    #         else:
    #             print('Data ',CariAngka,' tidak ditemukan')



    #Method pengurutan secara asc (min)
    def UrutAsc(self):
        if(self.Kosong()):
            print('Data Masih Kosong')
        else:
            i = self.Awal
            while(i.Next != None):
                min = i
                j = i.Next
                while(j != None):
                    if(j.Info < min.Info):
                        min = j
                    j = j.Next
                #proses pertukaran
                temp = min.Info
                min.Info = i.Info
                i.Info = temp
                #menempatkan pointer i ke simpul berikutnya
                i = i.Next


    #Method pengurutan secara desc (max)
    def UrutDesc(self):
        if(self.Kosong()):
            print('Data Masih Kosong')
        else:
            i = self.Awal
            while(i.Next != None):
                max = i
                j = i.Next
                while(j != None):
                    if(j.Info > max.Info):
                        max = j
                    j = j.Next
                #proses pertukaran
                temp = max.Info
                max.Info = i.Info
                i.Info = temp
                #menempatkan pointer i ke simpul berikutnya
                i = i.Next
            

#Badan program utama
#Inisialisasi linked list
List1 = SingleLinkedList()

Utama = 0
Utama = List1.MenuUtama(Utama)

while(Utama != 0):
    os.system('cls')
    match (Utama):
        case 1:
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

        case 2:
            print('-- Pengubahan Data --')
            AngkaBaru = int(input("Masukkan Angka Baru : "))
            List1.UbahData(AngkaBaru)
            print()
            List1.TampilData()
            print()
            os.system('pause')

        case 3:
            PilihHapus = 0
            PilihHapus = List1.MenuPenghapusan(PilihHapus)
            while(PilihHapus != 0):
                os.system('cls')
                match (PilihHapus):
                    case 1:
                        print('-- Pengahapusan Data di Depan --')
                        List1.HapusDepanSingle()
                        print()
                        List1.TampilData()
                        print()
                        os.system('pause')

                    case 2:
                        print('-- Pengahapusan Data di Belakang --')
                        List1.HapusBelakangSingle()
                        print()
                        List1.TampilData()
                        print()
                        os.system('pause')

                    case 3:
                        print('-- Pengahapusan Data di Tengah --')
                        List1.HapusTengahSingle()
                        print()
                        List1.TampilData()
                        print()
                        os.system('pause')

                PilihHapus = List1.MenuPenghapusan(PilihHapus)

        case 4:
            print('-- Pencarian Simpul --')
            List1.PecarianNode()
            print()
            List1.TampilData()
            print()
            os.system('pause')

        case 5:
            print('-- Pengurutan Data --')
            print('1. Asc')
            print('2. Desc')
            print('0. Keluar')
            PilihUrut = int(input("Pilihan Anda : "))
            while(PilihUrut != 0):
                os.system('cls')
                print('-- Angka Sebelum Terurut')
                List1.TampilData()
                print('')

                match (PilihUrut):
                    case 1:
                        print('-- Angka Setelah Terurut Secara Asc')
                        List1.UrutAsc()
                        List1.TampilData()
                        print('')
                    case 2:
                        print('-- Angka Setelah Terurut Secara Desc')
                        List1.TampilData()
                        print('')

                os.system('pause')
                os.system('cls')

                print('-- Pengurutan Data --')
                print('1. Asc')
                print('2. Desc')
                print('0. Keluar')
                PilihUrut = int(input("Pilihan Anda : "))

                
            print()
            List1.TampilData()
            print()
            os.system('pause')

    Utama = List1.MenuUtama(Utama)

#Memanggil method penghancuran
List1.Penghancuran()
print()
os.system('cls')
List1.TampilData()