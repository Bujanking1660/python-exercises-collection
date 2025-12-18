# fotocopy susah gampang
# I.S. : pengguna memasukkan tanggal transaksi(transaksi), status langganan(langganan), jumlah fotocopy(jumlah)
# F.S. : menampilkan tanggal transaksi, langganan, harga pelembar dan total bayar

# badan algoritma
tanggal   = str(input('Tanggal [dd/mm/yy] : '))
langganan = str(input('Langganan [Y/T]    : ')).upper()

'''
# validasi langganan
if(langganan != 'Y') and (langganan != 'T'):
    print('status langganan harus diisi dengan Y/T')
    exit()

# mengecek langganan untuk menentukan harga 
elif(langganan == 'Y'):
    # menentukan jumlah fotocopy
    jumlah = int(input('Jumlah fotocopy    : '))
    harga = 200

elif(langganan == 'T'):
    # menentukan jumlah fotocopy
    jumlah = int(input('Jumlah fotocopy    : '))
    if(jumlah < 100):
        harga = 300
    else:
        harga = 250
'''


# menyederhanakan if
# validasi langganan
if(langganan != 'Y') and (langganan != 'T'):
    print('status langganan harus diisi dengan Y/T')
    exit()
else:
    # menentukan jumlah fotocopy
    jumlah = int(input('Jumlah fotocopy    : '))
    # mengecek langganan untuk menentukan harga 
    match (langganan):
        case 'Y':
            harga = 200
            langganan = 'Berlangganan'
        case 'T':
            langganan = 'Belum Berlangganan'
            # mengecek jumlah fotocopy untuk menentukan harga
            if(jumlah < 100):
                harga = 300
            else:
                harga = 250

# menghitung total bayar
total = jumlah * harga

# menampilkan harga perlembar fotocopy, tanggal transaksi, langganan dan total bayar

print('----------------- Nota Fotocopy Susah Gampang ----------------')
print('Tanggal [dd/mm/yy] :',tanggal)
print('Langganan          :',langganan)
print('Harga Perlembar    : Rp.',harga)
print('Total bayar        : Rp.',total)
print('--------------------------------------------------------------')
print('❤ terima kasih ❤')