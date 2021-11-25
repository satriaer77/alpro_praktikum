def createMatriks(jmlBaris,jmlKolom) :
    matriks = []

    for i in range(jmlBaris) :
        for j in range(jmlKolom) :
            angka = int(input("==> Masukkan baris- %d kolom- %d =  " % (i,j)))
            matriks[i].append(angka)


    return matriks


print(createMatriks(2,3))
