Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:06:47) [MSC v.1914 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> Nama = "Mohammad Daffa Izzulhaq"
>>> NIM = 204
>>> Tinggi = 1.73
>>> Berat = 60
>>> TahunLahir = 2001
>>> Aku = (TahunLahir, Berat, Tinggi, NIM, Nama)
>>> Data = [TahunLahir, Berat, Tinggi, NIM, Nama]
>>> type (Aku)
<class 'tuple'>
>>> #Karena data "Aku" ditulis dengan tanda kurung biasa dan item didalamnya tidak dapat diubah
>>> Aku[0]
2001
>>> #Karena item pertama dari data "Aku" adalah "TahunLahir" dan nilainya adalah 2001
>>> a = NIM % 4; Aku[a]
2001
>>> #Karena sisa hasil dari 204 dibagi 4 adalah 0 dan data ke 0 dari variabel aku adalah 2001
>>> type(Aku[a])
<class 'int'>
>>> #Karena Aku[0] adalah "TahunLahir" dan nilainya adalah 2001 dimana 2001 bertipe data interger
>>> Aku[a:4]
(2001, 60, 1.73, 204)
>>> #Karena 4 item pertama dari data "Aku" adalah "TahunLahir", "Berat", "Tinggi", "NIM"
>>> type(Aku[4])
<class 'str'>
>>> #Karena item ke lima dari data "Aku" adalah "Nama", dan nilai dari "Nama" adalah "Mohammad Daffa Izzulhaq"

>>> Aku[0] = "ok"
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    Aku[0] = "ok"
TypeError: 'tuple' object does not support item assignment
>>> #Karena tipe data "Aku" adalah tuple yang mana isinya tidak dapat di ubah sehingga terjadi error
>>> type (Data)
<class 'list'>
>>> #Karena data "Data" ditulis dengan menggunakan kurung siku dan koleksi item didalamnya dapat berubah,bertambah dan berkurang secara dinamis
>>> type(Data[4])
<class 'str'>
>>> #Karena item ke lima dari data "Data" adalah "Nama" dan nilai dari "Nama" adalah "Mohammad Daffa Izzulhaq"
>>> Data[4][5]
'm'
>>> #Karena Data[4] atau objek ke lima dari "Data" adalah "Nama: dan indeks ke 5 dari "Nama" adalah "m"
>>> Data[4][a:6]
'Mohamm'
>>> #Karena Data[4] adalah "Nama" dan Nama[0:6] adalah objek pertama sampai objek ke enam dari "Nama" yaitu "Mohamm"
>>> Data[0]="ok";Data
['ok', 60, 1.73, 204, 'Mohammad Daffa Izzulhaq']
>>> #Karean tipe data dari variabel Data adalah list yang merupakan tipe data koleksi di mana objeknya dapat diubah
>>> Data[-a]
'ok'
>>> #Karena a adalah 0 jadi indeks 0 dari "Data" adalah objek pertama yaitu "ok"
>>> range(a)
range(0, 0)
>>> #Karena a adalah 0 jadi range(0) menghasilkan range 0 sampai 0
>>> 
