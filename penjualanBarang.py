# penjualan barang
# I.S. : pengguna memasukkan kode barang(kode), jumlah beli(jumlah), uang bayar(uang)
# F.S. : menampilkan kode barang, nama barang, jumlah, harga satuan, diskon, harga diskon, total, uang, kembalian

# badan algoritma

print('------Toko------')
print('Pakaian   : PK01')
print('Tas       : TS02')
print('Sepatu    : SP03')
print('Aksesoris : AK04')
print('----------------')
print('')


# menentukan kode barang
Kode = str(input('Masukkan Kode Barang : ')).upper()

# validasi kode barang
if(Kode != 'PK01') and (Kode!= 'TS02') and (Kode != 'SP03') and (Kode != 'AK04'):
    print('Kode barang tidak tersedia!')
    exit()
else:

    # menggunakan match case
    match(Kode):
        case 'PK01':
            Nama = 'pakaian'
            Harga = 75000
        case 'TS02':
            Nama = 'tas'
            Harga = 75000
        case 'SP03':
            Nama = 'sepatu'
            Harga = 75000
        case 'AK04':
            Nama = 'aksesoris'
            Harga = 75000

    '''
    # menggunakan if
    if(kode == 'PK01'):
        Nama = 'pakaian'
        Harga = 75000
    elif(kode == 'TS02'):
        Nama = 'tas'
        Harga = 65000
    elif(kode == 'SP03'):
        Nama = 'sepatu'
        Harga = 157000
    elif(kode == 'AK04'):
        Nama = 'aksesoris'
        Harga = 15000
    '''

# menentukan jumlah barang
Jumlah = int(input('Masukkan Jumlah Barang : '))
Diskon = 0
# mengecek jumlah untuk diskon
if(Jumlah < 10):
    Diskon = 0
else:
    # menentukan ada diskon atau tidak
    Keterangan = str(input('Adakah diskon [Y/T] :')).upper()

    # validasi keterangan diskon
    if(Keterangan != 'Y') and (Keterangan != 'T'):
        print('keterangan hanya bisa diisi dengan Y/T')
        exit()
    else:
        # menentukan diskon dengan satu kasus
        if(Keterangan == 'Y'):
            Diskon = int(input('Masukkan diskon :'))

# menghitung total bayar
Total = Jumlah * Harga

# menghitung total diskon
HargaDiskon = Total * (Diskon/100)

# menghitung total bayar di kurang total diskon
Total -= HargaDiskon


# menampilkan kode barang, nama barang, jumlah beli, diskon, harga diskon, harga barang, total bayar
print('---- nota penjualan ----')
print('kode barang  :',Kode)
print('nama barang  :',Nama)
print('jumlah beli  :',Jumlah,'pcs')
print('diskon',Diskon,'%  : Rp.', HargaDiskon)
print('harga barang : Rp.',Harga)
print('total bayar  : Rp. ',Total)
print('---------------------------------')

# memasukkan uang untuk membayar
Uang = int(input('Masukkan uang bayar : '))

# mengecek jika uang kurang
if(Uang < Total):
    print('Uang anda kurang!')
    exit()

# menghitung kembalian
Kembalian = Uang - Total

# menampilkan kembalian
print('kembalian : Rp. ',Kembalian)