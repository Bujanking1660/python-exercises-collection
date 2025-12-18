# I.S. : Array data belum terisi dan belum terurut
# F.S. : Menampilkan array berisi angka 1–12 sebagai kelas, diurutkan menggunakan metode Heap Sort

import os

class HeapSortKelas:
    def __init__(self):
        self.maksData = 12
        self.Data = [0 for _ in range(self.maksData)]

    def tampilkan_menu(self):
        print("<< MENU HEAP SORT KELAS >>")
        print("1. Isi Data")
        print("2. Tampilkan Data")
        print("3. Urutkan Data")
        print("0. Keluar")
        pilihan = int(input("Pilihan Anda: "))
        while pilihan < 0 or pilihan > 3:
            print("Pilihan hanya antara 0–3! Silakan ulangi.")
            pilihan = int(input("Pilihan Anda: "))
        return pilihan

    def tampilkan_submenu_urut(self):
        print("<< Menu Pengurutan >>")
        print("1. Urut Naik (Ascending)")
        print("2. Urut Turun (Descending)")
        sub = int(input("Pilihan Anda: "))
        while sub < 0 or sub > 2:
            print("Pilihan hanya antara 0–2! Silakan ulangi.")
            sub = int(input("Pilihan Anda: "))
        return sub

    def inisialisasi_data(self):
        for i in range(self.maksData):
            self.Data[i] = i + 1
        print(">> Data berhasil diisi dari kelas 1 hingga kelas 12.")

    def tampilkan_data(self):
        print("Isi array Data:")
        for i in range(self.maksData):
            print(f"Data[{i}] = kelas {self.Data[i]}")

    def tampilkan_binary_tree(self):
        N = len(self.Data)
        if N > 0:
            print(f"Root dari tree: kelas {self.Data[0]}")
            print()
        for i in range(N):
            kiri = 2 * i + 1
            kanan = 2 * i + 2
            print(f"Simpul: kelas {self.Data[i]}")
            if kiri < N:
                print(f" → Anak kiri  : kelas {self.Data[kiri]}")
            else:
                print(" → Anak kiri  : (tidak ada)")
            if kanan < N:
                print(f" → Anak kanan : kelas {self.Data[kanan]}")
            else:
                print(" → Anak kanan : (tidak ada)")
            print()

    def sift_down(self, i, N):
        lanjut = True
        while lanjut:
            kiri = 2 * i + 1
            kanan = 2 * i + 2
            terbesar = i

            if kiri < N and self.Data[kiri] > self.Data[terbesar]:
                terbesar = kiri
            if kanan < N and self.Data[kanan] > self.Data[terbesar]:
                terbesar = kanan

            if terbesar != i:
                self.Data[i], self.Data[terbesar] = self.Data[terbesar], self.Data[i]
                i = terbesar
            else:
                lanjut = False

    def susun_heap(self, N):
        for i in range((N // 2) - 1, -1, -1):
            self.sift_down(i, N)

    def heap_sort_descending(self):
        ukuranHeap = self.maksData
        self.susun_heap(ukuranHeap)
        for i in range(ukuranHeap - 1, 0, -1):
            print(f"Memindahkan root kelas {self.Data[0]} ke posisi {i}")
            self.Data[0], self.Data[i] = self.Data[i], self.Data[0]
            print("Array setelah langkah ini:")
            self.tampilkan_data()
            os.system('pause')
            ukuranHeap -= 1
            self.sift_down(0, ukuranHeap)
        
        for i in range((self.maksData - 1) // 2 + 1):
            self.Data[i], self.Data[self.maksData - 1 - i] = self.Data[self.maksData - 1 - i], self.Data[i]
        
        print("Array setelah dibalik untuk hasil urut turun:")
        self.tampilkan_data()
        os.system('pause')


    def heap_sort_ascending(self):
        ukuranHeap = self.maksData
        self.susun_heap(ukuranHeap)
        for i in range(ukuranHeap - 1, 0, -1):
            print(f"Memindahkan root kelas {self.Data[0]} ke posisi {i}")
            self.Data[0], self.Data[i] = self.Data[i], self.Data[0]
            print("Array setelah langkah ini:")
            self.tampilkan_data()
            os.system('pause')
            ukuranHeap -= 1
            self.sift_down(0, ukuranHeap)

        print("Array hasil urut naik:")
        self.tampilkan_data()
        os.system('pause')



# Program Utama
kelas = HeapSortKelas()
selesai = False

os.system('cls')
while not selesai:
    pilihan = kelas.tampilkan_menu()

    if pilihan == 1:
        os.system('cls')
        kelas.inisialisasi_data()
        os.system('pause')
        os.system('cls')
    elif pilihan == 2:
        os.system('cls')
        kelas.tampilkan_data()
        os.system('pause')
        os.system('cls')
    elif pilihan == 3:
        os.system('cls')
        sub = kelas.tampilkan_submenu_urut()
        if sub == 1:
            os.system('cls')
            kelas.heap_sort_ascending()
            print(">> Data telah diurutkan naik.")
            os.system('pause')
            os.system('cls')
        elif sub == 2:
            os.system('cls')
            kelas.heap_sort_descending()
            print(">> Data telah diurutkan turun.")
            os.system('pause')
            os.system('cls')
        else:
            os.system('cls')
            print("Pilihan tidak valid.")
            os.system('pause')
            os.system('cls')
    elif pilihan == 0:
        os.system('cls')
        os.system('pause')
        selesai = True
        print("Terima kasih. Program selesai.")
        os.system('cls')
