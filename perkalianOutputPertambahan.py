# Program menghitung perkalian dua angka dengan penjumlahan berulang

# Input dua angka dari pengguna
angka1 = int(input("Masukkan angka pertama: "))
angka2 = int(input("Masukkan angka kedua: "))

# Variabel untuk menyimpan hasil
hasil = 0

# For
# Menampilkan proses penjumlahan
print("\n", end="")
for i in range(angka2):
    hasil += angka1
    # Validasi untuk mengatur format output
    if i == angka2 - 1:  # Jika angka terakhir, tidak ada tanda +
        print(f"{angka1}", end="")
    else:
        print(f"{angka1} + ", end="")

# Menampilkan hasil akhir
print(f" = {hasil}")



hasil = 0

# While
# Menampilkan proses penjumlahan
a = 0 
while (a < angka2):
    hasil += angka1
    a += 1
    # Validasi
    if a == angka2:
        print(f"{angka1}",end="")
    else :
        print(f"{angka1} + ",end="")

print(f" = {hasil}")