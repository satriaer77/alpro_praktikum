
#Fungsi
def luasPersegiPanjang() :

    print("""

        ------ Anda Memilih Menu 2 (Luas Persegi Panjang) ------

            """)

    try : 
        panjang = float(input("==> Masukkan Panjang : "))
        lebar   = float(input("==> Masukkan Lebar   : "))
        
    
    except : 
        print("Yang Anda Masukkan bukan angka")
    
    else :
        luas    = panjang*lebar
    
        print("""

        ==> Rumus Luas Persegi Panjang  = P \u00d7 L

        +-----------+   Luas    = P \u00d7 L
        |           |           = %g \u00d7 %g
        |           |           = %g
        +-----------+
           
        ==> Jadi Luas Persegi Panjang dengan panjang %g dan lebar %g adalah %g <==

        """ % (panjang,lebar,luas, panjang,lebar,luas))



def luasLingkaran() :

    print("""

        ------ Anda Memilih Menu 1 (Luas Lingkaran) ------

            """)
    try : 
        pi          = 3.14
        jariJari    = float(input("==> Masukkan Jari-Jari : "))
    
    except : 
        print("Yang anda masukkan bukan angka")
    
    else : 
        luas = pi*jariJari**2
        print("""
        ==> Rumus Luas Lingkaran = \u03C0 \u00D7 r\u00B2  

          ____
         /    \   Luas  = 3.14 \u00D7 %g\u00B2
        |      |        = %g
         \____/ 

        ==> Jadi Luas Lingkaran dengan jari-jari %g adalah %g

                """ % (jariJari,luas,jariJari,luas))
        


def luasSegitiga() :

    print("""

        ------ Anda Memilih Menu 3 (Luas Segitiga) ------

            """)

    try :
        alas    = float(input("==> Masukkan Alas    : ")) 
        tinggi  = float(input("==> Masukkan Tinggi  : "))

    except :
        print("Yang Anda Masukkan Bukan angka")

    else : 
        luas = alas*tinggi/2

        print("""
        
        ==> Rumus Luas Segitiga = 1/2 \u00D7 Alas \u00D7 Tinggi

          /\    Luas    = 1/2 \u00D7 %g \u00D7 %g 
         /  \           = %g
        /____\

        ==> Jadi Luas Segitiga dengan alas %g dan tinggi %g adalah %g
                """ % (alas,tinggi,luas,alas,tinggi,luas))
#End Fungsi


#-=======================================================================-

error = 1

#Jalankan
while True : 
    try : 
        print("""
        
        +====== Program Penghitung Luas ======+
        |                                     |
        |   Menu                              |
        |   ----                              |
        |   1.) Luas Lingkaran                |
        |   2.) Luas Persegi Panjang          |
        |   3.) Luas Segitiga                 |
        |                                     |
        +=====================================+

        """)
        pilihan = int(input("==> Pilih menu program : "))
    
    except : 
        error+=1
        if(error >= 3) :
            print("Anda salah memasukkan inputan lebih dari 3x silahkan jalankan progam kembali")
            break
        else :
            print("Yang anda masukkan bukan angka silahkan coba lagi")
    
    else : 

        if pilihan == 1 :
            luasLingkaran()
        elif pilihan == 2 :
            luasPersegiPanjang()
        elif pilihan == 3 :
            luasSegitiga()
        else :
            print("Menu yang anda pilih tidak ada di daftar menu")


        lanjut = input("\n\nApakah anda ingin mengulangi program ini lagi y/t : ")
        if lanjut == 'y' :
            continue
        else : 
            break

    finally :
        print("Program Selesai dijalankan")




