#Program Perkalian Menggunakan Operator (+)
#I.S. : pengguna memasukkan nilai M dan N
#F.S. : menampilkan hasil dengan perkalian M dan N menggunakan operator penjumlahan (+)

import os
#badan program
print('---- Program Perkalian M dan N Menggunakan Operator (+) ----\n')
#memasukkan nilai M
M = int(input('Masukkan nilai M :'))

#validasi nilai M
while(M < 0) or (M > 20):
    print('Nilai M harus antara 1 sampai 20, Ulang!')
    os.system('pause')
    os.system('cls')

    #mengulangi
    print('---- Program Perkalian M dan N Menggunakan Operator (+) ----\n')
    #memasukkan nilai M
    M = int(input('Masukkan nilai M :'))



#memasukkan nilai N
N = int(input('Masukkan nilai N :'))

print(f'{M:<2} x {N:<2} = ',end='')

#validasi nilai M
while(N <= -5) or (N > 15):
    print('Nilai M harus antara -5 sampai 15, Ulang!')
    os.system('pause')
    os.system('cls')

    #mengulangi
    print('---- Program Perkalian M dan N Menggunakan Operator (+) ----\n')
    #menampilkan nilai M
    print('Nilai M :',M)
    #memasukkan nilai N
    N = int(input('Masukkan nilai N :'))

#menghitung M kali N menggunakan operator +
if(M == 0) or (N == 0):
    kali = 0
elif(M == 1):
    kali = N
else:
    kali = 0
    for i in range (M):
        print(N,end='')
        if(i < M-1):
            print(' + ',end='')
        kali += N
    print('\n        = ',end='')


#menampilkan hasil perkalian M dan N
print(f'{kali}')