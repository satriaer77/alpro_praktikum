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
Pertemuan   : 5
Tanggal     : September 23, 2021
Materi      : Algoritma

"""


#Fungsi Cek tahun kabisat
def cekKabisat(th) :
    if th % 4 == 0 :
        return "adalah tahun Kabisat"
    else :
        return "adalah bukan tahun Kabisat"
#End Cek fungsi tahun kabisat 

#Fungsi Cek tahun kabisat versi 2
def cekKabisat2(th) :
    if th % 4 != 0 :
        return "adalah bukan tahun Kabisat"
    else :
        return "adalah tahun Kabisat"
#End Cek fungsi tahun kabisat versi 2


#---------------------------------------------------#


#Jalankan
try :

    tahun= int(input("==>  Masukkan Tahun : "))

except :

    print("Yang anda masukkan bukan tahun")

else :

   print("""
   +----------------------------------------+
   |  Tahun %d %s |
   +----------------------------------------+
   """%(tahun,cekKabisat(tahun)))
