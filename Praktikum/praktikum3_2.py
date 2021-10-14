data = input("==> Masukkan Kata/Kalimat      : ")
cari = input("==> Masukkan huruf yang dicari : ")
i    = 0
a    = 1

for k in data : 
    if cari.lower() == k.lower():
        print("Huruf %s atau %s ke-%d : offset- %d" % (cari.lower(),cari.upper(),a,i))
        a+=1
    i+=1
    


