ak1 = 0                                                                                                                                                                   
ak2 = 1

def fibonacci(akg,a1,a2,htg) :
    hst=""
    while htg < akg:     
       hst      = hst+str(a1)
       hasilf   = a1 + a2
       a1       = a2
       a2       = hasilf
       htg      = htg+1
    print(hst)
    return hst


def cariAngka(cariAkg) :
    for i in range(0,len(hasilFibo)) :
        if cariAkg == hasilFibo[i] :
            print("Angka %d merupakan angka ke %d"%(hasilFibo,i+1))
            break



jmlAngka  = int(input("==>Masukkan jumlah angka : "))
hasilFibo = fibonacci(jmlAngka,ak1,ak2,ht)
cari      = input("==> Masukkan angka :")

cariAngka(cari)



