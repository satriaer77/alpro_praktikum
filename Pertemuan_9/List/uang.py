
uang        = [100000,50000,20000,10000,5000,2000,1000]
terbilang   = ["Seratus Ribu Rupiah", "Lima Puluh Ribu Rupiah", "Dua Puluh Ribu Rupiah","Sepuluh Ribu Rupiah", "Lima Ribu Rupiah","Dua Ribu Rupiah","Seribu Rupiah"]

banyakUang  = int(input("Masukkan Uang : Rp. "))

i = 0
while True :        
    jml     = banyakUang//uang[i]
    if jml != 0 :
        print(jml," Lembar ",terbilang[i])
    banyakUang = banyakUang%uang[i]

    if banyakUang == 0 :
        break
    elif banyakUang <1000 :
        print("Karena kami tidak mempunyai uang pecahan jadi sisanya kami donasikan sebesar Rp. ",banyakUang)
        break
    i+=1

