#Program Penjumlahan Angka 1 Sampai 10
#I.S. : diberikan nilai pencacah(i) = 10
#F.S. : menampilkan hasil penjumlahan(Hasil) = 1+2+3...+10

#badan program 
print('---- Program Penjumlahan Angka 1 Sampai 10 ----')
print('\n')

#for positif
print('<<< Pengulangan For Positif >>>')
print('Hasil = ',end='')
Hasil = 0
for i in range(1,11):
    print(i,end='')
    if(i < 10):
        print(' + ',end='')
    Hasil += i

#menampilkan hasil variable Hasil
print('\n      = ',Hasil)


print('\n')


#for negatif
print('<<< Pengulangan For Negatif >>>')
print('Hasil = ',end='')
Hasil = 0
for i in range(10,0,-1):
    print(i,end='')
    if(i > 1):
        print(' + ',end='')
    Hasil += i

#menampilkan hasil variable Hasil
print('\n      = ',Hasil)


print('\n')


#while naik
print('<<< Pengulangan While Cacah Naik >>>')
print('Hasil = ',end='')
Hasil = 0
i = 1
while (i <= 10):
    print(i,end='')
    if(i < 10):
        print(' + ',end='')
    Hasil += i
    i += 1

#menampilkan hasil variable Hasil
print('\n      = ',Hasil)


print('\n')


#while turun
print('<<< Pengulangan While Cacah Turun >>>')
print('Hasil = ',end='')
Hasil = 0
i = 10
while (i >= 1):
    print(i,end='')
    if(i > 1):
        print(' + ',end='')
    Hasil += i
    i -= 1

#menampilkan hasil variable Hasil
print('\n      = ',Hasil)