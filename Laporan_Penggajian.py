#Laporan_Penggajian

# I.S. : pengguna memasukkan bulan, tahun, penggajian, tiga data karyawan yang terdiri dari NIK, Nama, Gaji Pokok.}
# F.S. : menampilkan data per karyawan dan total gaji yang harus dibayar oleh perusahaan.}

import os

#Badan Program

# memasukkan bulan dan tahun penggajian
Bulan = str(input('Bulan (nama bulan) :'))
Tahun = str(input('Tahun (nama tahun) :'))



# memasukkan
print('---- Data Penggajian Karyawan Pertama ----')
NIK1            = str(input('Nomor Induk Karyawan (NIK)  :'))
Nama1           = str(input('Nama Karyawan               :'))
GajiPokok1      = float(input('Gaji Pokok Karyawan         : Rp.'))
# menghitung pajak, tunjangan, dan gaji bersih
PPN1       = 0.1 * GajiPokok1
Tunjangan1 = 0.2 * GajiPokok1
GajiBersih1 = GajiPokok1 + Tunjangan1 - PPN1
# menampilkan data gaji karyawan
os.system('cls')
print('---- Data Penggajian Karyawan Pertama ----')
print(f'NIK         : {NIK1}')
print(f'Nama        : {Nama1}')
print(f'Gaji Pokok  : Rp. {GajiPokok1:>14}')
print(f'Pajak       : Rp. {PPN1:>14,.1f}')
print(f'Tunjangan   : Rp. {Tunjangan1:>14,.1f}')
print(f'Gaji bersih : Rp. {GajiBersih1:>14,.1f}')
os.system('pause')
os.system('cls')



# memasukkan
print('---- Data Penggajian Karyawan Kedua ----')
NIK2            = str(input('Nomor Induk Karyawan (NIK)  :'))
Nama2           = str(input('Nama Karyawan               :'))
GajiPokok2      = float(input('Gaji Pokok Karyawan         : Rp.'))
# menghitung pajak, tunjangan, dan gaji bersih
PPN2       = 0.1 * GajiPokok2
Tunjangan2 = 0.2 * GajiPokok2
GajiBersih2 = GajiPokok2 + Tunjangan2 - PPN2
# menampilkan data gaji karyawan
os.system('cls')
print('---- Data Penggajian Karyawan Kedua ----')
print(f'NIK           : {NIK2}')
print(f'Nama Karyawan : {Nama2}')
print(f'Gaji Pokok    : Rp. {GajiPokok2:>14}')
print(f'Pajak         : Rp. {PPN2:>14,.1f}')
print(f'Tunjangan     : Rp. {Tunjangan2:>14,.1f}')
print(f'Gaji bersih   : Rp. {GajiBersih2:>14,.1f}')
os.system('pause')
os.system('cls')



# memasukkan
print('---- Data Penggajian Karyawan Ketiga ----')
NIK3            = str(input('Nomor Induk Karyawan (NIK)  :'))
Nama3           = str(input('Nama Karyawan               :'))
GajiPokok3      = float(input('Gaji Pokok Karyawan         : Rp.'))
# menghitung pajak, tunjangan, dan gaji bersih
PPN3       = 0.1 * GajiPokok3
Tunjangan3 = 0.2 * GajiPokok3
GajiBersih3 = GajiPokok3 + Tunjangan3 - PPN3
# menampilkan data gaji karyawan
os.system('cls')
print('---- Data Penggajian Karyawan Pertama ----')
print(f'NIK           : {NIK3}')
print(f'Nama Karyawan : {Nama3}')
print(f'Gaji Pokok    : Rp. {GajiPokok3:>14}')
print(f'Pajak         : Rp. {PPN3:>14,.1f}')
print(f'Tunjangan     : Rp. {Tunjangan3:>14,.1f}')
print(f'Gaji bersih   : Rp. {GajiBersih3:>14,.1f}')
os.system('pause')
os.system('cls')


# menampikan tabel laporan penggajian karyawan
print('========================================================================================================')
print('                                      Laporan Gaji Karyawan                                             ')
print(f"Bulan/Tahun : {Bulan:>8}/{Tahun:>4}")
print('')
print('---------------------------------------------------------------------------------------------------------')
print('|    NIK   |     Nama Karyawan    |   Gaji Pokok    |      Pajak      |    Tunjangan    |   Gaji Bersih   |')
print('---------------------------------------------------------------------------------------------------------')
print(f'| {NIK1:8} | {Nama1:20} | Rp. {GajiPokok1:>11,.0f} | Rp. {PPN1:>11,.1f} | Rp. {Tunjangan1:>11,.1f} | Rp. {GajiBersih1:>11,.1f} |')
print('---------------------------------------------------------------------------------------------------------')
print(f'| {NIK2:8} | {Nama2:20} | Rp. {GajiPokok2:>11,.0f} | Rp. {PPN2:>11,.1f} | Rp. {Tunjangan2:>11,.1f} | Rp. {GajiBersih2:>11,.1f} |')
print('---------------------------------------------------------------------------------------------------------')
print(f'| {NIK3:8} | {Nama3:20} | Rp. {GajiPokok3:>11,.0f} | Rp. {PPN3:>11,.1f} | Rp. {Tunjangan3:>11,.1f} | Rp. {GajiBersih3:>11,.1f} |')
print('---------------------------------------------------------------------------------------------------------')

# menghitung total gaji yang harus dibayar perusahaan
Total_Gaji = GajiBersih1 + GajiBersih2 + GajiBersih3

# menampilkan total gaji yang harus dibayar perusahaan
print(f'Total Gaji Bersih Karyawan  : Rp. {Total_Gaji:>14,.1f}')
print('========================================================================================================')
