
def jmlLembar(bu,ug,tn) :
    i = 0
    while True :
        jml     = bu//ug[i]
        if jml != 0 :
            print(jml," Lembar ",tn[i])
        bu = bu%ug[i]
    
        #print(banyakUang)

        if bu == 0 :
            break
        elif bu <1000 :
            print("Karena kami tidak mempunyai uang pecahan jadi sisanya kami donasikan sebesar Rp. ",bu)
            break
        i+=1


uang        = [100000,50000,20000,10000,5000,2000,1000]
terbilang   = ["Seratus Ribu Rupiah", "Lima Puluh Ribu Rupiah", "Dua Puluh Ribu Rupiah","Sepuluh Ribu Rupiah", "Lima Ribu Rupiah","Dua Ribu Rupiah","Seribu Rupiah"]


try : 
    banyakUang  = int(input("Masukkan Uang : Rp. "))

except :
    print("Yang Anda Masukkan Bukan Angka")

else :

    jmlLembar(banyakUang,uang,terbilang)



