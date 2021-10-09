#Fungsi cek max angka dengan kondisional
def cekMaxAl(akg1,akg2,akg3,akg4) :
    if akg1 > akg2 and akg1 > akg3 and akg1 > akg4:
        nilai = akg1
        inp = '1'
                
    elif akg2 > akg1 and akg2 > akg3 and akg2 > akg4:
        nilai = akg2
        inp = '2'
    
    elif akg3 > akg1 and akg3 > akg3 and akg3 > akg4 :
        nilai = akg3
        inp = '3'

    else :
        nilai = akg4 
        inp = '4'

    print(""" 
        +---------------------------------------------------------------+   
        |  Angka inputan %s merupakan angka max antara %d,%d,%d,%d dengan nilai %d |
        +---------------------------------------------------------------+
        """ % (inp,akg1,akg2,akg3,akg4,nilai))

       
#End cek max angka



#Fungsi cek max angka dengan kondisional v2
def cekMaxAl2(akg1,akg2,akg3,akg4) :
    if akg1 > akg2 :
        nilai = akg1
        inp = '1'
                
    elif akg2 > akg1 :
        nilai = akg2
        inp = '2'
        
       
    if nilai < akg3 and akg3 > akg4:
        nilai = akg3
        inp = '3'
   
    elif nilai < akg4 :
        nilai = akg4
        inp = '4'


    print(""" 
        +---------------------------------------------------------------+   
        |  Angka inputan %s merupakan angka max antara %d,%d,%d,%d dengan nilai %d |
        +---------------------------------------------------------------+
        """ % (inp,akg1,akg2,akg3,akg4,nilai))
       
#End cek max angka





#-------------------------

#Jalankan
try :

    a1 = int(input("==> Masukkan angka ke1 : ")) #ambil data dari inputan user dengan tipe data int
    a2 = int(input("==> Masukkan angka ke2 : ")) 
    a3 = int(input("==> Masukkan angka ke3 : ")) 
    a4 = int(input("==> Masukkan angka ke4 : ")) 

except:#tampilkan ini bila yang user masukkan bukan angka

    print("Yang anda masukkan bukan angka")

else:
    cekMaxAl2(a1,a2,a3,a4)

