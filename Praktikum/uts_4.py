bilTerakhir = int(input("Bilangan Terakhir : "))
hasil = ""
bnyk = 0
for i in range(bilTerakhir+1) :
    if i % 2 == 0 :
        hasil = hasil+str(i)+" "
        bnyk+=1


print("""

Bilangan : %s
Banyaknya Bilangan Genap : %d

        """ % (hasil,bnyk) ) 
