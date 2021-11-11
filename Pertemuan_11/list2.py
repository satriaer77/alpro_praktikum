def tambahElemenList(no,jmlAngka) :
    data       = []
    for i in range(jmlAngka) :
        angka = int(input("==> Masukkan Data%d Angka ke- %d: "%(no,i+1)))
        data.append(angka)
    return data

def penjumlahanList(lists1,lists2) :
    hasil = []
    if len(lists1) == len(lists2) :
       for i in range(len(lists1)) :
            hasil.append(lists1[i]+lists2[i])

    else :
        print("Len list tidak sama")

    return hasil
 
jmlAngka    = int(input("==> Masukkan jumlah angka yang akan diinput : "))

list1       = tambahElemenList(1,jmlAngka)
list2       = tambahElemenList(2,jmlAngka)

print("",penjumlahanList(list1,list2))
