angka       = int(input("==> Masukkan angka : "))
jmlEksponen = int(input("==> Masukkan jumlah eksponen : "))

def eksponen(akg,jEks) : #diambil dari var angka dan jml eksponen
    hasil = 1
    for i in range(jEks) :
        hasil = hasil*angka

    return hasil


print(eksponen(angka,jmlEksponen)) #menampilkan hasil dari eksponen
