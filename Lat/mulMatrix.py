def createMatrix(baris,kolom) :
    matrix = []
    for i in range(baris) :
        listBaris = []
        for j in range(kolom) :
            listBaris.append(int(input("==> Angka [%d,%d] : "%(i,j))))
        matrix.append(listBaris)
    return matrix



def mulMatrix(matrix1,matrix2) :
    baris = len(matrix1[0]) == len(matrix2)

    if baris :
        hasil = []
        for i in range(len(matrix1)) :
            tmpHasil = []
            for j in range(len(matrix2[0])) :
                total = 0
                for k in range(len(matrix1)) :
                    total+= matrix1[i][k]*matrix2[k][j]
                tmpHasil.append(total)
            hasil.append(tmpHasil)
        return hasil
    else :
        return "Tidak sama"



mat1 = [[3,1,6],[2,10,3],[4,1,5]]#createMatrix(2,2)
mat2 = [[3,4,0],[9,10,11],[3,12,7]]#createMatrix(1,2)

#print(mat1)
print(mulMatrix(mat1,mat2))
