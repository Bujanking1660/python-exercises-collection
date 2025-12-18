# Program Menghitung Bayar Parkir berdasarkan Kendaraan dan Lama Parkir
# I.S. : pengguna memasukkan jenis kendaraan(Kendaraan), nomor polisi(nopol), waktu masuk(JamMasuk dan MenitMasuk), waktu keluar(JamKeluar dan WaktuKeluar)
# F.S. : menampilkan jenis kendaraan,nomor polisi, waktu masuk, waktu keluar, lama parkir, dan biaya yang harus dibayar


# badan algoritma
print('--------------------- Biaya Parkir ---------------------------')
Kendaraan    = str(input('Masukkan jenis kendaraan (motor/mobil)   : ')).upper()
nopol        = str(input('Masukkan Nomor Polisi                    : '))
print('-------------------------------------------------------------')
JamMasuk     = int(input('Masukkan jam masuk                       : '))
MenitMasuk   = int(input('Masukkan menit masuk                     : '))
print('-------------------------------------------------------------')
JamKeluar    = int(input('Masukkan jam keluar                      : '))
MenitKeluar  = int(input('Masukkan menit keluar                    : '))

# menentukan lama parkir
if(MenitKeluar < MenitMasuk):
    MenitKeluar = MenitKeluar + 60
    JamMasuk = JamKeluar - 1

Menit = MenitKeluar - MenitMasuk

if(JamKeluar < JamMasuk):
    JamKeluar = JamKeluar + 12

Jam = JamKeluar - JamMasuk

# mengubah jam jika menit parkir lebih dari nol

if(Menit > 0):
    Jam = Jam + 1

# menentukan jenis kendaraan
if(Kendaraan == "MOTOR"):
    Biaya = 1500 + (Jam - 1)*500
else:
    Biaya = 3000 + (Jam - 1)*1000

# menampilkan jenis kendaraan, waktu masuk, waktu keluar ,lama parkir dan biaya
print('-------------------------------------------------------------')
print('Jenis Kendaraan             :',Kendaraan)
print('Nomor Polisi                :',nopol)
print('Waktu Masuk                 :',JamMasuk,':',MenitMasuk)
print('Waktu Keluar                :',JamKeluar,':',MenitKeluar)
print('Lama Parkir                 :',Jam,'Jam')
print('Biaya yang harus di bayar   : Rp.',Biaya)
print('-------------------------------------------------------------')
 