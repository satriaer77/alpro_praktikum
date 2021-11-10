jmlMhs          = int(input("-> Masukkan Jumlah Mahasiswa : "))
namaMahasiswa   = []
nilaiMahasiswa  = []
char            = 0

for i in range(jmlMhs) :
    print("\n\n+-------- Mahasiswa %d ---------+" % (i))
    namaMahasiswa.append(input("==> Masukkan Nama Mahasiswa : "))
    nilaiMahasiswa.append(int(input("==> Masukkan Nilai Mahasiswa : ")))
    
    if i != 0 :
        if len(namaMahasiswa[i-1]) > len(namaMahasiswa[i]) :
            char = len(namaMahasiswa[i])
        else :
            char = len(namaMahasiswa[i])


for naM,niM in namaMahasiswa,nilaiMahasiswa :

    print("""
+--%s Daftar Nama dan Nilai Mahasiswa %s--+
|  Nama %s |  Nilai %s |
+--%s+--%s+
| %s | %s |
+--%s+--%s+
""" % ('-'*char,'-'*char,' '*char,' '*char,' '*char,' '*char,naM,niM,'-'*char,'-'*char))

