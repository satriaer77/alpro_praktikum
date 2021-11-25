hari                   = ("Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu", "Minggu")
hariPertama     = input("==> Masukkan informasi, hari pertama bulan ini, jatuh pada hari : ")
tanggal             = int(input("==> Masukkan tanggal yang ingin diketahui harinya : "))
indexHari         = hari.index(hariPertama)-1

for i in range(tanggal) :
    indexHari+=1
    if indexHari == 7 :
        indexHari = 0

print("Tanggal %d adalah hari %s"%(tanggal,hari[indexHari]))
