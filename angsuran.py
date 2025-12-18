# Program Menghitung Angsuran dan Bunga Motor

def login():
    # Login sederhana dengan batas percobaan 3 kali
    username = "user"
    password = "123"

    error = 1
    while error <= 3:
        input_username = input("Masukkan Nama Pengguna: ")
        input_password = input("Masukkan Kata Sandi: ")
        
        if input_username == username and input_password == password:
            print("Login Berhasil")
            break
        else:
            print("Nama Pengguna atau Kata Sandi salah.")
            error += 1

        if error > 3:
            print("Login gagal!\n")
            exit()


def hitung_angsuran(harga_motor, uang_muka, lama_angsuran):
    # Hitung angsuran per bulan
    sisa_harga = harga_motor - uang_muka
    angsuran_per_bulan = sisa_harga / lama_angsuran

    # Hitung bunga per bulan
    bunga_per_bulan = (uang_muka + (angsuran_per_bulan * lama_angsuran) - harga_motor) / harga_motor * 100

    return angsuran_per_bulan, bunga_per_bulan

def tampilkan_angsuran(harga_motor, uang_muka, lama_angsuran):
    angsuran_per_bulan, bunga_per_bulan = hitung_angsuran(harga_motor, uang_muka, lama_angsuran)

    print(f"\nRincian Angsuran:")
    print(f"Harga Motor: Rp {harga_motor}")
    print(f"Uang Muka: Rp {uang_muka}")
    print(f"Lama Angsuran: {lama_angsuran} bulan")
    print(f"Angsuran Per Bulan: Rp {angsuran_per_bulan:.2f}")
    print(f"Bunga Per Bulan: {bunga_per_bulan:.5f}%\n")

    print("Daftar Angsuran:")
    sisa_hutang = harga_motor - uang_muka
    for bulan in range(1, lama_angsuran + 1):
        print(f"Bulan {bulan}: Rp {angsuran_per_bulan:.2f}, Sisa Hutang: Rp {sisa_hutang:.2f}")
        sisa_hutang -= angsuran_per_bulan

def main():
    if login():
        # Input data motor dan angsuran
        print("Masukkan Data Motor dan Angsuran")
        merk_motor = input("Merk Motor: ")
        harga_motor = float(input("Harga Motor: Rp "))
        uang_muka = float(input("Uang Muka (DP): Rp "))
        lama_angsuran = int(input("Lama Angsuran (bulan): "))

        # Tampilkan rincian dan daftar angsuran
        tampilkan_angsuran(harga_motor, uang_muka, lama_angsuran)
    else:
        print("Program berakhir.")

if __name__ == "__main__":
    main()