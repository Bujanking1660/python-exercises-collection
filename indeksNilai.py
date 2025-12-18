# Indeks Nilai

# I.S. : pengguna memasukkan nilai
# F.S. : menampilkan nilai dan indeks nilai

# badan program
print('---- indeks nilai ----')
nilai = float(input('Masukkan nilai :'))

'''
# integer
nilai = int(input('Masukkan nilai :'))
# menentukan indeks nilai
if(nilai >= 80) and (nilai <= 100):
    indeks = 'A'
elif (nilai >= 70) and (nilai <= 79):
    indeks = 'B'
elif (nilai >= 60) and (nilai <= 69):
    indeks = 'C'
elif (nilai >= 50) and (nilai <= 59):
    indeks = 'D'
else:
    indeks = 'E'
'''

'''
# float
nilai = float(input('Masukkan nilai :'))
# menentukan indeks nilai
if(nilai >= 80) and (nilai <= 100):
    indeks = 'A'
elif (nilai >= 70) and (nilai < 80):
    indeks = 'B'
elif (nilai >= 60) and (nilai < 70):
    indeks = 'C'
elif (nilai >= 50) and (nilai < 60):
    indeks = 'D'
else:
    indeks = 'E'
'''


# menyederhanakan majemuk menjadi tunggal
if(80 <= nilai <= 100):
    indeks = 'A'
elif (70 <= nilai < 80):
    indeks = 'B'
elif (60 <= nilai < 70):
    indeks = 'C'
elif (50 <= nilai < 60):
    indeks = 'D'
elif (0 <= nilai < 50):
    indeks = 'E'
else: # validasi nilai
    indeks = 'Nilai harus antara 0 - 100 !'


print(f'indeks : {indeks}')
