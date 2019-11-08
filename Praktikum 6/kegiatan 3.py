Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:06:47) [MSC v.1914 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> Nama = "Mohammad daffa izzulhaq"
>>> NIM = "L200190204"
>>> X = "1" + NIM[7:]
>>> a = int (X)
>>> b = len(Nama)
>>> type (a)
<class 'int'>
>>> #Karena data "X" telah berubah menjadi type data interger
>>> type(b)
<class 'int'>
>>> #Karena data "Nama" memiliki instruksi "len"
>>> a / b
52.34782608695652
>>> #Karena hasil dari 1204 dibagi 23 adalah 52.34782608695652
>>> a // b
52
>>> #Karena arti dari "//" pembagian dengan pembulatan
>>> 10 * (a - 999)
2050
>>> #Karena nilai "a" dikurangi 999 adalah 205, kemudian dikalikan dengan 10 dan hasilnya 2050
>>> b ** 2
529
>>> #Karena arti dari "**" adalah perpangkatan
>>> a % b
8
>>> #Karena arti "%" adalah sisa hasil bagi
>>> c = 12.5
>>> type (c)
<class 'float'>
>>> #Karena 12.5 adalah bilangan desimal
>>> a / c
96.32
>>> #Karena hasil dari 1204 dibagi 12.5 adalah 96.32
>>> a // c
96.0
>>> #Karena arti dari "//" adalah pembagian dengan pembulatan
>>> a % c
4.0
>>> #Karena arti "%" adalah sisa hasil bagi dan sisa dari 1204 dibagi 12.5 adalah 4.0
>>> c > b
False
>>> #Karena nilai "c" lebih besar dari nilai "b" adalah salah
>>> type(c > b)
<class 'bool'>
>>> #Karena c > b hanya memiliki dua kemungkinan yaitu true atau false
>>> a > b and b > c
True
>>> #Karena logika "DAN" true and true memnghasilkan nilai true
>>> a > 1100 or b < 10
True
>>> #Karena logita "ATAU" true or false menghasilkan nilai true
>>> 
