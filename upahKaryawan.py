# upah karyawan
# I.S. :
# F.S. :

# badan algoritma

namaKaryawan = str(input('Masukkan Nama Karyawan      :'))
jamKerja     = int(input('Masukkan Jam Kerja Per Hari :'))
upah   = 1000000


lembur = jamKerja * 7
if(jamKerja > 40):
    lembur - 40
    upah = upah * (lembur * 2)

print('Nama Karyawan      :',namaKaryawan)
print('Lama Lembur        :',jamKerja * 7 - 40,'jam')
print('Upah yang diterima :', upah) 