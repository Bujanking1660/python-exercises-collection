# program menghitung upah per minggu yang diterima oleh seorang karyawan
# I.S : pengguna memasukkan berapa jam bekerja dalam sehari
# F.S : menampilkan nama karyawan, keterangan dan upah yang di dapat


# badan algoritma
print('Upah Karyawan : 500.000 / minggu')
Upah = 500000
NamaKaryawan = str(input('Masukkkan nama karyawan    : '))
JamKerja     = int(input('Masukkan jam kerja perhari : '))


# mengubah dari jam kerja per hari menjadi per minggu
JamKerja = JamKerja * 7


Keterangan  = 'tidak_lembur'
if(JamKerja > 40):
    Lembur = JamKerja - 40
    Lembur * 2 
    Keterangan = 'Lembur'

print('Nama Karyawan     :',NamaKaryawan)
print('Keterangan        :',Keterangan)
print('Waktu Lembur      :',Lembur)
print('Upah yang didapat :',Lembur*Upah)