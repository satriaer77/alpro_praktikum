data1       = []
data2       = []
dataHasil   = []
jmlAngka    = int(input("==> Masukkan jumlah angka yang akan diinput : "))


for i in range(jmlAngka) :
    angka1 = int(input("==> Masukkan Data1 Angka ke- %d: "%(i+1)))
    data1.append(angka1)
    
    angka2 = int(input("==> Masukkan Data2 Angka ke- %d: "%(i+1)))
    data2.append(angka2)

for j in range(len(data1)) :
    for h in range(len(data2)) :
        if i == h :
            dataHasil.append(data1[j]+data2[h])
            print(data1[h])

print("""
data1 = %s
data2 = %s

hasil jumlah = %s

        """%(data1,data2,dataHasil))


