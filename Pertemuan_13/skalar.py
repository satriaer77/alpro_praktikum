a       = [[2,3,4],[5,6,7]]
skr     = 2

def skalar(matrix,skl) :
    for i in range(len(matrix)) :
        for j in range(len(matrix)+1) :
            matrix[i][j] = matrix[i][j] * skl
    return matrix

print(skalar(a,skr))
