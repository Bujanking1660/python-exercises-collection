# program seleksi pemilu
# I.S. : pengguna memasukkan umur dan status pernikahan
# F.S. : menampilkan boleh memilih atau tidak

# badan program
print('---- seleksi ikut pemilu ----')
umur = int(input('Masukkan umur :'))
if(umur < 17):
    menikah = str(input('Masukkan status menikah [Y/T] :')).upper()

    # menyederhanakan bentuk if
    match (menikah):
        case 'Y':
            print('Anda boleh ikut pemilu')
        case 'T':
            print('Anda belum boleh ikut pemilu')
        case _  :
            print('status menikah harus diisi dengan Y/T')
            exit()

    '''
    if(menikah == 'Y'):
        print('Anda boleh ikut pemilu')
    elif (menikah == 'T'):
        print('Anda belum boleh ikut pemilu')
    else:
        print('status menikah harus diisi dengan Y/T')
        exit()
    '''


else:
    print('Anda boleh ikut pemilu')


