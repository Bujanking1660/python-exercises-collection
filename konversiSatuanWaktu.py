# Mengubah Satuan Detik Menjadi Satuan Hari, Jam, Menit dan Detik
# I.S. : pengguna memasukkan satuan detik untuk diubah ke satuan hari, jam, menit dan detik
# F.S. :

#badan algoritma

detik = int(input('Masukkan Satuan Detik : '))

#mengubah ke hari
hari = detik // (24 * 3600)

#mengubah ke jam
detik = detik % (24 * 3600)
jam   = detik // 3600

#mengubah ke menit
detik = detik % 3600
menit = detik // 60

#mengubah ke detik
detik = detik % 60
detik = detik 

print('Hari  :', hari)
print('Jam   :', jam)
print('Menit :', menit)
print('Detik :', detik)