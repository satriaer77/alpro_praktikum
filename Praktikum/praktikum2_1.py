try : 
    akg = int(input("Masukkan angka : "))
except :
     print("Yang anda masukkan bukan angka")

else :
    
    prime = False
    if akg > 1:
        for i in range(2, akg):
            if (akg % i) == 0:
                prime = True
                break

    if prime:
        print(akg, "Adalah Bukan Bilangan Prima ")
    else:
        print(akg, "Adalah Bilangan Prima")
