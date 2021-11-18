import 
from modul import buatList

sys.path.append('../funcModul.py')


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

list1       = buatList(jmlAngka)
list2       = buatList(jmlAngka2)

print("",penjumlahanList(list1,list2))
