hari                = ("Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu", "Minggu")
hariPertama  = input("==> Masukkan hari pertama pada bulan ini = ")
indexHari      = hari.index(hariPertama)-1
tanggal          = int(input("==> Masukkan Tanggal = "))


for i in range(tanggal) :
    indexHari += 1
    if indexHari == 7 :
        indexHari = 0


print("Tanggal %d adalah hari %s" % (tanggal,hari[indexHari]))

