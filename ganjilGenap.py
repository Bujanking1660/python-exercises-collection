# Program Menentukan Bilangan Ganjil atau Genap
# I.S. : pengguna memasukkan sebuah bilangan
# F.S. : menampilkan keterangan "Bilangan Genap" atau "Bilagan Ganjil"

# Badan Algortima
# memasukkkan bilangan
Bilangan = int(input('Masukkan Sebuah Bilangan : '))

# menentukan bilangan genap atau ganjil
if (Bilangan % 2 == 0):
    Keterangan = 'Bilangan Genap'
else:
    Keterangan = 'Bilagan Ganjil'
# menampilkan isi keterangan
print(Bilangan,'adalah',Keterangan)