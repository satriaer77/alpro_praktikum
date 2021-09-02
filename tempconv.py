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


=== Tugas Konversi Temperatur Celcius ke farenheit ===
Pertemuan   : 2
Tanggal     : September 2, 2021
Materi      : Tipe Data, Variabel, dan Operator

"""



try :
    celsius = float(input("==>  Masukkan suhu celsius : ")) #Mengambil inputan suhu celsius dari user

except : #Mencetak error yang digunakan bila inputan tidak sesuai dengan tipe data float
    print("Yang anda masukkan bukan angka")

else : #Kode ini dijalankan bila tidak ada error dari inputan celsius
    
    #Cek suhu minus
    if celsius < -273 : #bila suhu inputan kurang dari -273 maka blok kode ini akan dijalankan
        print("Batas suhu paling dingin adalah -273\u00b0 C")
        celsius = -273 #Data suhu di inputan user akan ditimpa dengan nilai -273
    #End cek suhu minus

    convfarenheit = (9/5 * celsius) +32 #Rumus konversi suhu Celsius ke Farenheit
    print("""
    
    Rumus Konversi Celsius ke Farenheit
    +-------------------+
    | F = (9/5 \u00D7 %g)+32 |
    +-------------------+

     _
    | |  Suhu Celsius = %g\u00b0 C 
    | |  
    |i|  F = (9/5 \u00D7 %g)+32
   /iii\\   = %g\u00b0 F
   \iii/
    \-/
    
    Konversi Celsius ke Farenheit
    =--------------------------------------------=
    Jadi suhu %g\u00b0 C  ke Farenheit adalah  %g\u00b0 F
    =--------------------------------------------=


    """ % (celsius,celsius,celsius,convfarenheit,celsius,convfarenheit))



#Penjelasan Code
"""
Untuk mengkonversi suhu dari celcius ke farenheit data yang dibutuhkan adalah :
- data suhu celsius
- data hasil konversi dari celsius ke farenheit

yang pertama adalah mendefinisikan variable celcius dengan nilai inputan angka bertipe data float dari user,
--------------
celsius = float(input('Masukkan suhu celsius : '))
--------------

sebelum perintah di blok else dijalankan variable celsius akan di check terlebih dahulu
apakah ada error (yaitu kesalahan inputan dari user)
-----
Menggunakan error handling seperti yang sudah saya jelaskan di atas
-----

contoh user memasukkan huruf di inputan
variable celcius dan itu akan dideteksi error karena yang nilai yang seharusnya dimasukkan itu adalah
float
contoh :
------------
Masukkan suhu celsius : 4a
------------

bila nilai sudah benar betipe float kemudian akan dijalankan perintah yang ada di blok else
kemudian dilakukan pengecekan nilai apakah nilai tersebut sesuai ketentuan kurang dari -273
bila tidak maka dijalankan blok kode yang ada di if, jika tidak kode didalam blok if tersebut tidak dijalankan

Kemudian tampilkan outputnya menggunakan perintah print untuk cara yang saya gunakan adalah
menggunakan penformatan placeholder

untuk sumber yang saya gunakan untuk penformatan dari
- https://stackoverflow.com/questions/4288973/whats-the-difference-between-s-and-d-in-python-string-formatting

untuk sumber symbol yang saya gunakan
- https://en.wikipedia.org/wiki/List_of_Unicode_characters

sumber suhu terdingin yang bisa dicapai
- https://www.sciencedaily.com/releases/2013/01/130104143516.htm

sumber rumus konversi celsius ke farenheit
- https://rumusrumus.com/rumus-c-ke-f/
"""
