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


=== Tugas Konversi US Dollar ke Rupiah ===
Pertemuan   : 2
Tanggal     : September 2, 2021
Materi      : Tipe Data, Variabel, dan Operator

"""


kursRupiah = 14268.80 # Kurs 1 US Dollar ke Rupiah

try :
    dollar =float(input("===> Masukkan jumlah dollar : ")) #Mengambil inputan dollar dari user dengan tipe data float
    
except :#Mencetak error yang digunakan bila inputan tidak sesuai dengan tipe data float
    print("Input yang anda masukkan bukan angka!")
    
else :#Kode ini dijalankan bila tidak ada error dari inputan dollar
    konversi = kursRupiah*dollar
    print("""
    
     $
    $$$
   $       Konversi = dollar \u00D7 kursrupiah
    $$$             = %g \u00D7 %s 
       $            = Rp. %s
    $$$ 
     $

    =----------------------------------------------------=
    Jadi hasil konversi dari $->Rp. adalah $%s ==> Rp. %s
    =----------------------------------------------------=


    """ % (dollar,kursRupiah,konversi,dollar,konversi))

    

#Penjelasan Code
"""
Untuk menghitung konversi US dollar ke rupiah data yang dibutuhkan adalah :
- data kurs US dollar ke rupiah
- data jumlah dollar


Pertama kita definisikan variabel kursRupiah dengan nilai 14628.80 , kemudian
kita definisikan variabel dollar dengan nilai inputan dari user
+--------+
dollar =float(input("===> Masukkan jumlah dollar : "))
+--------+

sebelum perintah di blok else dijalankan, variable dollar akan di check terlebih dahulu
apakah ada error (yaitu kesalahan inputan dari user)
-----
Menggunakan error handling seperti yang sudah saya jelaskan di atas
-----

contoh user memasukkan huruf di inputan variable dollar dan itu akan dideteksi error karena yang nilai 
yang seharusnya dimasukkan itu adalah float
contoh :
------------
Masukkan jumlah dollar : 100r
------------

bila nilai sudah benar betipe float kemudian akan dijalankan perintah yang ada di blok else
Kemudian tampilkan outputnya menggunakan perintah print untuk cara yang saya gunakan adalah
menggunakan penformatan placeholder



sumber symbol yang saya gunakan
- https://en.wikipedia.org/wiki/List_of_Unicode_characters (List of Unicode characters)

sumber yang saya gunakan untuk penformatan dari
- https://stackoverflow.com/questions/4288973/whats-the-difference-between-s-and-d-in-python-string-formatting (What's the difference between %s and %d in Python string formatting?)

sumber error handling
- https://docs.python.org/3/tutorial/errors.html (8. Errors and Exceptions)


"""
