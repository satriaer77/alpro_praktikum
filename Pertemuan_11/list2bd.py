def tambahElemenList(no,jmlAngka) :
    data       = []
    for i in range(jmlAngka) :
        angka = int(input("==> Masukkan Data%d Angka ke- %d: "%(no,i+1)))
        data.append(angka)
    return data

def penjumlahanList(lists1,lists2) :
    hasil = []

    if len(lists1) >= len(lists2) :
        listTinggi = lists1
        listRendah = lists2
    else :
        listTinggi = lists2
        listRendah = lists1

    for i in range(len(listTinggi)) :
        if i < len(listRendah) :
            hasil.append(listTinggi[i]+listRendah[i])
        else :
            hasil.append(listTinggi[i])
    return hasil
 

jmlAngka    = int(input("==> Masukkan jumlah angka yang akan diinput : "))
jmlAngka2   = int(input("==> Masukkan jumlah angka2 yang akan diinput : "))

list1       = tambahElemenList(1,jmlAngka)
list2       = tambahElemenList(2,jmlAngka2)

print("",penjumlahanList(list1,list2))
