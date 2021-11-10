jmlMhs          = int(input("-> Masukkan Jumlah Mahasiswa : "))
namaMahasiswa   = []
nilaiMahasiswa  = []
char            = 0
jml             = 0

for i in range(jmlMhs) :
    print("\n\n+-------- Mahasiswa %d ---------+" % (i+1))
    namaMahasiswa.append(input("==> Masukkan Nama Mahasiswa : "))
    nilaiMahasiswa.append(int(input("==> Masukkan Nilai Mahasiswa : ")))
    jml = jml+nilaiMahasiswa[i]
    if i != 0 :
        if len(namaMahasiswa[i-1]) > len(namaMahasiswa[i]) :
            char = len(namaMahasiswa[i])
        else :
            char = len(namaMahasiswa[i])





rata    = jml/len(nilaiMahasiswa)

print("\n\n----> Daftar Mahasiswa <----")
for i in range(len(namaMahasiswa)) :
    print("Nama Mahsiswa = %s , Nilai = %s" % (namaMahasiswa[i],nilaiMahasiswa[i]))

print("""

Nilai Rata-rata = %f 
-- Daftar Mahasiswa yang nilanya diatas rata-rata --
""" % (rata))

for i in range(len(namaMahasiswa)) :
    if nilaiMahasiswa[i] >= rata :
        print("- ",namaMahasiswa[i])

