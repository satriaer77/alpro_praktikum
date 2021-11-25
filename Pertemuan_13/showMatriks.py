def creatematriks2D(a,b): 
    baris=[] 
    for i in range(a): 
        kolom=[] 
        for k in range(b): 
            x='masukkan baris ke-'+str(i)+'kolom ke'+str(k)+'=' 
            user=int(input(x)) 
            kolom.append(user) 
        baris.append(kolom) 
    
    return baris 

def showMatrix(matrix) :
    for i in range(len(matrix)) :
        print(str(matrix[i]).replace(","," "))



def showMatrix2(matrix) :
    tmpS = ""

    for i in range(len(matrix)) :
        for j in range(len(matrix[i])) :

            if j == 0 :
                tmpS = tmpS+"| "

            tmpS = tmpS+str(matrix[i][j])+"  "
            
            if j == len(matrix[i])-1 :
                tmpS = tmpS+"| \n"

    return tmpS


def showMatrix2_1(matrix) :
   
    for i in range(len(matrix)) :
        tmpS = ""
        for j in range(len(matrix[i])) :
            tmpS = tmpS+str(matrix[i][j])+"  "
        print(tmpS)        
    


matrix = creatematriks2D(2,3) 
print("\n\n --- Matriks %d x %d ---- \n\n"  % (len(matrix),len(matrix[0])) )
#showMatrix(matrix)

print(showMatrix2(matrix))
showMatrix2_1(matrix)
