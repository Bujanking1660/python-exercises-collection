angka1 = int(input('Masukkan nilai ke-1 : '))
angka2 = int(input('Masukkan nilai ke-2 : '))

operator = str(input('Masukkan operator tambah(+), kurang(-), kali(x), bagi(:)'))

if(operator == '+'):
    hasil = angka1 + angka2
elif(operator == '-'):
    hasil = angka1 - angka2
elif(operator == 'x'):
    hasil = angka1 * angka2
elif(operator == ':'):
    hasil = angka1 / angka2
else:
    print('harap masukkan operator sesuai!')


print(hasil)