# -*- coding: utf-8 -*-
"""

pppp   y   y  ttttttt  h     h   ooooo   n   n  
p  p    y y      t     h hhh h  o     o  n n n 
ppp      y       t     h     h  o     o  n  nn
p        y       t     h     h   ooooo   n   n 

+--------------------------------+
| NAMA    : Bima Satria Erlangga |
| NIM     : 210411100085         |
| PRODI   : Teknik Informatika   |
+--------------------------------+


=== Tugas Menghitung Luas Lingkaran ===
Pertemuan   : 2
Tanggal     : September 2, 2021
Materi      : Tipe Data, Variabel, dan Operator

"""



pi = 3.14 #variabel pi 

try :
    r = float(input("==> Masukkan Jari-jari : ")) #Mengambil inputan dari user dengan tipe data float

except :
    print("Yang anda masukkan bukan angka!")

else :#Kode ini dijalankan bila tidak ada error dari inputan r
    
    luas=pi*r**2 #Rumus Luas Lingkaran
    
    #Menampilkan Hasil
    print(""" 
      Luas Lingkaran
     +-------------+
     | L = \u03C0 \u00D7 r\u00B2  |
     +-------------+
    
      0000     
    0      0     r = %g
    0      0     L = %s \u00D7 %d\u00B2
      0000         = %s

    =---------------------------------------------=
    Jadi luas lingkaran berjari-jari %g adalah %s
    =---------------------------------------------=

    """ % (r,pi,r,luas,r,luas))
    #End Menampilkan Hasil


#Penjelasan Kode
"""
Untuk menghitung luas lingkaran data yang dibutuhkan adalah :
- pi
- jari - jari

Pertama kita definisikan variabel pi dengan nilai 3.14, kemudian
kita definisikan variabel r (jari-jari)
+--------+
r = float(input("==> Masukkan Jari-jari : "))
+--------+

sebelum perintah di blok else dijalankan, variable r akan di check terlebih dahulu
apakah ada error (yaitu kesalahan inputan dari user)
-----
Menggunakanerror handling seperti yang sudah saya jelaskan di atas
-----

contoh user memasukkan huruf di inputan variable r dan itu akan dideteksi error karena yang nilai yang seharusnya dimasukkan itu 
adalah float
contoh :
------------
Masukkan jari-jari : 4.3aw
------------

bila nilai sudah benar betipe float kemudian akan dijalankan perintah yang ada di blok else
Kemudian tampilkan outputnya menggunakan perintah print untuk cara yang saya gunakan adalah
menggunakan penformatan placeholder



sumber symbol yang saya gunakan
- https://en.wikipedia.org/wiki/List_of_Unicode_characters (List of Unicode characters)

sumber yang saya gunakan untuk penformatan dari
- https://stackoverflow.com/questions/4288973/whats-the-difference-between-s-and-d-in-python-string-formatting (What's the difference between %s and %d in Python string formatting?)

sumber rumus luas lingkaran
- https://www.kelaspintar.id/blog/tips-pintar/empat-cara-menghitung-luas-lingkaran-1306/ (Empat Cara Mudah untuk Menghitung Luas Lingkaran)
 
sumber error handling
- https://docs.python.org/3/tutorial/errors.html (8. Errors and Exceptions)


"""




