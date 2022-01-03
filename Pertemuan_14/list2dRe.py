def createList1D(ukuranList) :
    temp = []
    for i in range(ukuranList) :
        inp = "Masukkan data ke-"+str(i)+"="
        temp.append(int(input(inp)))

    return temp

def dispList1D(ls) :
    tempStr=''
    for i in range(len(ls)) :
        tempStr = tempStr+" "+str(ls[i])+" "
    tempStr = "| "+tempStr+" |"
    print(tempStr)


def createList2D(jmlBar,jmlKolom) :
    temp = []
    for baris in range(jmlBar) :
        print("Pengisian data baris ke-",baris)
        temp.append(createList1D(jmlKolom))
    return temp


def dispList2D(matrix) :
    for i in range(len(matrix)) :
        tmpS = ""
        for j in range(len(matrix[i])) :

            tmpS = tmpS+str(matrix[i][j])+"  "
          
        print("| "+tmpS+"|")

def dispList2D1(matrix):
    for baris in matrix :
        dispList1D(baris)


#mat = createList1D(2)
mat2 = createList2D(3,2)

dispList2D1(mat2)
