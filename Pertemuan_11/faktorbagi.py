def faktorPembagi(bil) :
    faktorBagi = []
 
    for i in range(1,bil+1) :
        if bil%i == 0 :
            faktorBagi.append(i)

    return faktorBagi

bilangan = int(input("==> Masukkan bilangan  : "))

print(faktorPembagi(bilangan))
