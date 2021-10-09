#Fungsi cek max angka dengan list
def cekMax(akg1,akg2,akg3) :
    listakg = [akg1,akg2,akg3]
    print("Angka Maksimum dari 3 inputan adalah",max(listakg))
#End fungsi cek max angka

#----------------


#Fungsi cek max angka dengan kondisional
def cekMaxAl(akg1,akg2,akg3) :
    if akg1 > akg2 and akg1 > akg3 :

        print("""
        +-----------------------------------------------------+ 
        | Angka inputan 1 merupakan angka max dengan nilai %d | 
        +-----------------------------------------------------+
        """%(akg1))
        
    elif akg2 > akg1 and akg2 > akg3 :
       
        print("""
        +-----------------------------------------------------+
        | Angka inputan 2 merupakan angka max dengan nilai %d |
        +-----------------------------------------------------+
        """%(akg2))
    
    else :
        print(""" 
        +-----------------------------------------------------+   
        | Angka inputan 3 merupakan angka max dengan nilai %d |
        +-----------------------------------------------------+
        """ % (akg3))

#End cek max angka



#Fungsi cek max angka dengan kondisional v2
def cekMaxAl2(akg1,akg2,akg3) :
    if akg1 > akg2 and akg1 > akg3 :
        nilai = akg1
        inp = '1'
                
    elif akg2 > akg1 and akg2 > akg3 :
        nilai = akg2
        inp = '2'
            
    else :
        nilai = akg3  
        inp = '3'

    print(""" 
        +-----------------------------------------------------+   
        |  Angka inputan %s merupakan angka max dengan nilai %d |
        +-----------------------------------------------------+
        """ % (inp,nilai))
       
#End cek max angka


#Fungsi cek max angka dengan kondisional v3
def cekMaxAl3(akg1,akg2,akg3) :
    if akg1 > akg2 :
        nilai = akg1
        inp = '1'
                
    else :
        nilai = akg2
        inp = '2'
        
       
    if nilai < akg3 :
        nilai = akg3
        inp = '3'
   
    print(""" 
        +---------------------------------------------------------------+   
        |  Angka inputan %s merupakan angka max antara %d,%d,%d dengan nilai %d |
        +---------------------------------------------------------------+
        """ % (inp,akg1,akg2,akg3,nilai))
       
#End cek max angka



#Fungsi cek max angka dengan kondisional v4
def cekMaxAl4(akg1,akg2,akg3) :
    if akg1 > akg2 :
        nilai = akg1
        inp = '1'
                
    elif akg2 > akg1 :
        nilai = akg2
        inp = '2'
         
    elif nilai < akg3 :
        nilai = akg3
        inp = '3'
   
    print(""" 
        +---------------------------------------------------------------+   
        |  Angka inputan %s merupakan angka max antara %d,%d,%d dengan nilai %d |
        +---------------------------------------------------------------+
        """ % (inp,akg1,akg2,akg3,nilai))
       
#End cek max angka




#-------------------------

#Jalankan
try :

    a1 = int(input("==> Masukkan angka ke1 : ")) #ambil data dari inputan user dengan tipe data int
    a2 = int(input("==> Masukkan angka ke2 : ")) 
    a3 = int(input("==> Masukkan angka ke3 : ")) 

except:#tampilkan ini bila yang user masukkan bukan angka

    print("Yang anda masukkan bukan angka")

else:
    cekMaxAl3(a1,a2,a3)

