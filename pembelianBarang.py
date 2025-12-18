# Pembelian Barang

# {I.S. : pengguna memasukkan }
# {F.S. : menampilkan }

kode   = str(input('Masukkan kode barang     :')).upper()

if(kode == 'PK01'):
    nama = 'pakaian'
    harga = 75000
else:
    if(kode == 'TS02'):
        nama = 'Tas'
        harga = 65000
    else:
        if(kode == 'SP03'):
            nama = 'Sepatu'
            harga = 157000
        else:
            if(kode == 'AK04'):
                nama = 'Aksesoris'
                harga = 45000
            else:
                print('kode tidak ada!');
                harga = 0

jumlah = int(input('Masukkan jumlah barang   :'))

if(jumlah < 10):
    diskon = 0
else:
    keterangandiskon = str(input('Ada diskon [Y/T] :'))
    if(keterangandiskon == 'Y'):
        diskon = int(input('Masukkan diskon :'))
    else:
        if(keterangandiskon == 'T'):
            diskon = 0
        else:
            print('keterangan diskon di isi Y/T')

     
    

total = jumlah * harga 
hargadiskon = total *(diskon/100)
total = total - hargadiskon

print('Kode Barang  :',kode)
print('Nama Barang  :',nama)
print('Jumlah Beli  :',jumlah)
print('Harga Satuan :',harga)
print('Diskon',diskon,'%   :',hargadiskon)
print('Total Bayar  :',total)
print('--------------------------')
uang   = int(input('Masukkan uang pembayaran :'))
kembalian = uang - total
print('Bayar        :',uang)
print('Kembalian    :',uang-total)
