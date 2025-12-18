# 1) Berapa total percobaan login gagal di server hari itu
akun = ["akun 1","akun 2","akun 3","akun 4","akun 5"]
login_gagal = [3,7,1,9,2]

print(akun)
print(login_gagal)

# 2) Hitung total login gagal
total = 0
for i in login_gagal:
    total += i
print("Total gagal :", total)

# 3) Hitung rata rata login gagal
rata = total / len(login_gagal)
print('Rata rata login gagal per akun :',rata)

# 4) Cari akun dengan login gagal terbanyak
max_gagal = login_gagal[0]
akun_max = akun[0]

for i in range (len(login_gagal)):
    if(login_gagal[i] > max_gagal):
        max_gagal = login_gagal[i]
        akun_max = akun[i]

print("Akun dengan login gagal terbanyak :", akun_max, "-", max_gagal, "kali")

# 5) Cari akun mencurigakan
print("Akun mencurigakan (lebih dari 5 gagal)")
for i in range (len(login_gagal)):
    if(login_gagal[i] > 5):
        print("-", akun[i], ":", login_gagal[i], "kali")

for n in range(len(login_gagal)):
    print(akun[n],end='')
    for k in range (1,login_gagal[n]):
        print('*',end='')