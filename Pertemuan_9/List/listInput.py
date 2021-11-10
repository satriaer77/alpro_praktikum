listAngka   = []
listGenap   = []
jmlAngka    = int(input("==> Masukkan jumlah angka yang akan diinput : "))

for i in range(jmlAngka) :
    angka = int(input("==> Masukkan Angka : "))
    listAngka.append(angka)
    if angka %2 == 0 :
        listGenap.append(angka)

print("\n\nAngka Genap : ")
if len(listGenap) > 0 :
    for genap in listGenap :
        print(genap," ",end='')


