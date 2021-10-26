bil1 = int(input("==> Masukkan bilangan 1 : "))
bil2 = int(input("==> Masukkan bilangan 2 : "))
faktorPembagi1 = []
faktorPembagi2 = []
fbp = []

def faktorBagi (bil,fb) :
    for a in range(1,bil+100) :
        if bil%a == 0 :
            fb.append(a)
    

    print("Faktor Pembagi %d : %s" % (bil,fb))

def fpbFc(fb1,fb2,fpb) :
    if fb1 > fb2 :
        for b1 in fb1 :
            for b2 in fb2 :
                if b1 == b2 :
                    #print(b1)
                    fpb.append(b1)
    else :
        for b2 in fb2 :
            for b1 in fb1 :
                if b1 == b2 :
                    fpb.append(b2)


faktorBagi(bil1,faktorPembagi1)
faktorBagi(bil2,faktorPembagi2)

fpbFc(faktorPembagi1,faktorPembagi2,fbp)

print("Pembagi yang sama = %s ; FPB : %d " % (fbp,max(fbp)))



