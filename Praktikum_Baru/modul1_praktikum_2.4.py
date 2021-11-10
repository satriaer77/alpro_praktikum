n = int(input("==> Masukkan nilai n : ")) #digunakan untuk menentukan banyaknya angka yang akan ditampilkan
a = int(input("==> Masukkan nilai a : ")) #digunakan untuk menentukan nilai awal
b = int(input("==> Masukkan nilai b : ")) #digunakan untuk menentukan nilai beda

for i in range(1,n+1) :
    un = a+(i-1)*b
    print("u- %d = %d "%(i,un))

sn = n/2*(2*a+(n-1)*b)
print("=> Sn = ",sn)
