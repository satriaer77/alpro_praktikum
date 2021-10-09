#Fungsi Rumus

def formula(batas) :
    jml = 0

    for i in range(1,batas+1):
        rumus   = 2*(i) + 4
        jml     = jml+rumus
        print(rumus)

        if(i == batas) :
             print(""" 
+------------+
 Total : """,jml)



def formulanb(batas) :
    ht=""
    jml = 0
    for i in range(1,batas+1):
        rumus = 2*(i) + 4
        jml = jml+rumus
        ht = ht+" "+str(rumus)
        if(i == batas) :
            print(ht)
            print(""" 
+------------+
 Total : """,jml)


 
def formulaintv(batas) :
    ht=""
    jml = 0
    for i in range(1,batas+1):
        jml = jml
        ht = ht+" "+str(rumus)
        if(i == batas) :
            print(ht)
            print(""" 
+------------+
 Total : """,jml)           


def formulawhl(batas) :
    ht      = ""
    jml     = 0
    indeks  = 1

    while indeks <= batas+1:
        rumus   = 2*(indeks) + 4
        jml     = jml+rumus
        ht      = ht+" "+str(rumus)
        indeks += 1
        if(indeks == batas) :
            print(ht)
            print(""" 
+------------+
 Total : """,jml)   



def formulaex(batas,nx) :
    ht=""
    jml = 0
    for i in range(1,batas+1):
        rumus = i**2
        jml = jml+rumus
        ht = ht+" "+str(rumus)
        if(i == batas) :
            print(ht)
            print(""" 
+-------------------+
 Total : %d + %d = %d """% (jml,nx,jml+nx) )


#End Fungsi


#===============================



#Jalankan
try :
    pilih = int(input(""" 

Pilih Menu Rumus :
1. \u03A32i + 4
2. x + \u03A3i\u00B2

Pilih Menu : """))

    print("""

 Anda Memilih Menu %d
+---------------------+

"""% (pilih))
    
    if(pilih == 1) :
        n   = int(input("==> Masukkan nilai n : "))

    elif(pilih == 2) :
        n   = int(input("==> Masukkan nilai n : "))
        x   = int(input("==> Masukkan nilai x : "))
        
    frm = "x + \u03A3i\u00B2"

except :
    print("Yang anda masukkan bukan angka!")

else :
    
    if(pilih == 1) :
        print("""
+----------------+    
| n       = %d   |
| Formula = 2i+4 |
+----------------+

           """ % (n))
        formulaintv(n)


    elif(pilih == 2) :

        print("""
+---------------------+    
| n       = %d        |
| x       = %d        |
| Formula = %s   |
+---------------------+

            """ % (n,x,frm))
        formulaex(n,x)

    else :
        print("Menu yang anda masukkan tidak ada di pilihan")
