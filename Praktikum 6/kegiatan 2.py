## Program Akun
## Dibuat oleh Daffa L200190204
import random
angka = random.randint(0,1000)

Nama = "Mohammad Daffa Izzulhaq"
TanggalLahir = "23 Mei 2001"
NamaSingkat = Nama[0]+"."+Nama[9]+"."+Nama[15:23]
Username = Nama [0] + TanggalLahir[:2] + TanggalLahir [7:11]
Password = Nama[0:3] + str(angka)

print (Nama)
print (TanggalLahir)
print (NamaSingkat)
print (Username)
print (Password)
