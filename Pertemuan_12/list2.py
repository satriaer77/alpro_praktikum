import modul as md

def penjumlahanList(lists1,lists2) :
    hasil = []
    if len(lists1) == len(lists2) :
       for i in range(len(lists1)) :
            hasil.append(lists1[i]+lists2[i])

    else :
        print("Len list tidak sama")

    return hasil
 
jmlAngka    = int(input("==> Masukkan jumlah angka yang akan diinput : "))

list1       = md.buatList(jmlAngka)
list2       = md.buatList(jmlAngka)
print("",penjumlahanList(list1,list2))
