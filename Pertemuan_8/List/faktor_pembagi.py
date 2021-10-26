bil = int(input("==> Masukkan bilangan : "))
faktorPembagi = []

for a in range(1,bil+100) :
    if bil%a == 0 :
        faktorPembagi.append(a)


print("""
        Bilangan %d mempunyai %d faktor Pembagi, yaitu 
        Faktor Pembagi : %s
        """ % (bil,len(faktorPembagi),faktorPembagi))

