#Fotocopy Susah Gampang

#{ I.S. : pengguna memasukkan tanggal transaksi(tanggal), status langganan(langganan), jumlah fotocopy(jumlah)}
#{ F.S. : menampilkan tanggal transaksi dan total bayar}

#badan program
print('---- Fotocopy Susah Gampang ----')

#daerah masukkan
tanggal   = str(input('Masukkan tanggal transaksi                   :'))
langganan = str(input('Apakah kamu langganan [Y/T]                  :')).upper()


#validasi
if(langganan != 'Y') and (langganan != 'T'):
    print('Status Langganan hanya dapat di isi dengan "Y" dan "T" ')
else:
    jumlah    = int(input('Masukkan berapa lembar yang akan di fotocopy :'))
    if(langganan == 'Y'):
        harga = 200
    else:
        if(jumlah < 100):
            harga = 300
        else:
            harga = 250

totalbayar = jumlah * harga
print('--------------------------------')
print('Tanggal Transaksi :',tanggal)
print('Total Bayar       :',totalbayar)