def faktorial(akg):
    if akg==0 :
        faktor=1
    else : 
        faktor  =1
        for i in range(akg,0,-1):
            print(i)
            faktor  = faktor*i
        
    return(faktor)


angka   = int(input("==> Masukkan bilangan = "))
hasil   = faktorial(angka)
print(angka,"! =",hasil)
