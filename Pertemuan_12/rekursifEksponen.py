ak = 2 #angka
ek = 5 #eksnpoen

def eksponen(a,e) : #fungsi rekursif
    if e == 0 :
        return 1
    else :
        return a*eksponen(a,e-1) #memanggil fungsi kembali

print(eksponen(ak,ek)) #tampilkan hasil
