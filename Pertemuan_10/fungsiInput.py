jmlAngka    = int(input("==> Masukkan jumlah angka yang akan diinput : "))

def listAngkaGenap(jmlAkg) :
    listGenap   = []

    for i in range(1,jmlAkg+1) :
        angka = int(input("==> Masukkan Angka ke %d: "%(i)))
        if angka %2 == 0 :
            listGenap.append(angka)

    return listGenap


def printGenap(lsGenap) :
    print("\n\nAngka Genap : ")
    if len(listGenap) > 0 :
        for genap in listGenap :
            print(genap," ",end='')
    else :
        print("listGenap tidak mempunyai data angka genap")

listGenap = listAngkaGenap(jmlAngka)
printGenap(listGenap)
