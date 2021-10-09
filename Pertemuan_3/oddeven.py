#Fungsi buat cek angka ambil dari inputan user
def cekAngka(angka) :

    if(angka %2 == 0) :#cek angka bila genap
        print("""
        === Angka %d yang anda masukkan termasuk angka genap ===
        """ % (angka))
    else :
        print("""
        === Angka %d yang anda masukkan termasuk angka ganjil ===
        """ % (angka))




try :

    akg = int(input("==> Masukkan angka : ")) #ambil data dari inputan user dengan tipe data int

except:#tampilkan ini bila yang user masukkan bukan angka

    print("Yang anda masukkan bukan angka")

else:
    cekAngka(akg)
    

