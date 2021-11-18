#Fungsi Prima
def primeNum(akg) :
        prime = True
        if akg > 1:
            for i in range(2, akg):
                if (akg % i) == 0:
                    prime = False 
                    break

        if prime:
            print(akg, "Adalah Bilangan Prima ")
        else:
            print(akg, "Adalah Bukan  Bilangan Prima")

#End Fungsi rPima


angka = int(input("==> Masukkan Angka : "))

primeNum(angka)

#primeNum(int(input("==> Masukkan Angka :")))
