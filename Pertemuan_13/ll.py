matrix = [[2,4,5],[6,4,1]]

for i in range(len(matrix)) :
    tmpS = ""
    for j in range(len(matrix[i])) :

        #if j == 0 :
         #   tmpS = tmpS+"| "

        tmpS = tmpS+str(matrix[i][j])+"  "
            
       # if j == len(matrix[i])-1 :
        #    tmpS = tmpS+"| \n"

    print("| "+tmpS+"|")

