#Program Penentuan Toko Termurah
#I.S : pengguna memasukkan data pelanggan, data bahan baku, data toko, data kebutuhan bahan baku per pelanggan dan data harga bahan baku per toko
#F.S : menampilkan toko termurah untuk per pelanggan

import os

#konstanta
MaksPelanggan = 6
MaksBahan = 5
MaksToko = 3

#Subrutin memasukkan semua data yang digunakan
def IsiData(P,B,T,kebutuhan,harga):
    os.system('cls')
    print(f'---- Pengisian data pelanggan sebanyak {MaksPelanggan} data ----')
    for i in range(MaksPelanggan):
        P[i] = str(input('Nama Pelanggan ke-{}:'.format(i+1)))

    os.system('cls')
    print(f'---- Pengisian data bahan baku sebanyak {MaksBahan} data ----')
    for j in range(MaksBahan):
        B[j] = str(input('Bahan baku ke-{}:'.format(j+1)))

    os.system('cls')
    print(f'---- Pengisian data kebutuhan sebanyak {MaksPelanggan} data ----')
    for i in range(MaksPelanggan):
        print(f'Kebutuhan pelanggan {P[i]}')
        for j in range(MaksBahan):
            kebutuhan[i][j] = int(input('Jumlah bahan baku {}:'.format(B[j])))
        print()

    os.system('cls')
    print(f'---- Pengisian data toko sebanyak {MaksToko} data ----')
    for k in range(MaksToko):
        T[k] = str(input('Toko ke-{}:'.format(k+1)))

    os.system('cls')
    print(f'---- Pengisian data harga bahan baku per toko ----')
    for j in range(MaksBahan):
        print(f'Kebutuhan bahan baku {B[j]}')
        for k in range(MaksToko):
            harga[j][k] = int(input('Harga di Toko {} : Rp').format(B[j]))
    
#Subrutin menghitung kebutuhan dengan harga (TotalHarga)
def TotalHarga(kebutuhan,harga,hasil):
    print('Perhitungan total harga para pelanggan per toko')
    for i in range(MaksPelanggan):
        print(f'Total Harga Pelanggan {P[i]}')
        for k in range(MaksToko):
            hasil[i][k] = 0
            for j in range(MaksBahan):
                hasil[i][k] = hasil[i][k] + kebutuhan[i][j] * harga[j][k] 
            
            print(f'Total harga di toko {T[k]} = Rp. {hasil[i][k]:,}')
        print()


#Subrutin menentukan total harga termurah
def Termurah(hasil,murah):
    print(f'---- Penentuan total harga termurah per pelanggan ----')
    for i in range(MaksPelanggan):
        min = hasil[i][0]
        murah[i] = 0
        for k in range(1,MaksToko):
            if(hasil[i][k] < min):
                min = hasil[i][k]
                murah[i] = k

        print(f'Total harga termurah untuk {P[i]} : Rp. {min:,}')

#Subrutin menampilkan toko termurah
def TampilTokoTermurah(murah):
    print('Rekomendasi toko termurah per pelanggan')
    for i in range(MaksPelanggan):
        print(f'Pelanggan {P[i]} direkomendasikan ke ',end='')
        if(murah == 0):
            print('Toko 1')
        elif(murah == 1):
            print('Toko 2')
        else:
            print('Toko 3')


#Badan Program Utama

#Penciptaan data pelanggan(P)
P = ['/'] * MaksPelanggan

#Penciptaan data bahan baku(B)
B = ['/'] * MaksBahan

#Penciptaan data kebutuhan bahan baku
kebutuhan = [0] * MaksPelanggan
for j in range (MaksPelanggan) :
    kebutuhan[j] = [0] * MaksBahan

#Penciptaan data toko(T)
T = ['/'] * MaksToko

#Penciptaan data harga bahan baku per toko
harga = [0] * MaksBahan
for k in range(MaksBahan):
    harga[k] = [0] * MaksToko

#Penciptaan data hasil perkalian matriks (hasil)
hasil = [0] * MaksPelanggan
for k in range(MaksPelanggan):
    hasil[k] = [0] * MaksToko

#Penciptaan data termurah (murah)
murah = [0] * MaksPelanggan

#Memanggil subrutin memasukkan semua data yang digunakan
IsiData(P,B,T,kebutuhan,harga)

#Memanggil subrutin menghitung total harga (perkalian matriks kebutuhan dengan matriks harga)
TotalHarga(kebutuhan,harga,hasil)

#Memanggil subrutin total harga toko termurah
Termurah(hasil,murah)

#Memanggil subrutin menampikan toko termurah
TampilTokoTermurah(murah)