def matr(baris,kolom) :
    for i in range(baris) :
        for j in range(kolom) :
            print("[%d,%d] "%(i,j),end="" )
            if j == kolom-1 :
                print("\n")

matr(2,2)
