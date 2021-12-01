class Matrix :

    @staticmethod
    def createMatrix2D(baris,kolom) :
        matrix = []
        for i in range(baris) :
            bar = []
            for j in range(kolom) :
                bar.append(int(input("==> Mat[%d,%d] : " % (i,j) )))
            
            matrix.append(bar)

        return matrix



    @staticmethod
    def dispMatrix2D(listMatrix) :
        strMatrix = ""
        pjgMax    = 0
        for i in range(len(listMatrix)) : 
            if pjgMax <= len(str(max(listMatrix[i]))) :              
                pjgMax = len(str(max(listMatrix[i])))
                
        print(pjgMax,"\n")
        for baris in listMatrix :
            
            for kolom in baris :
                if baris.index(kolom) == 0 :
                    strMatrix = strMatrix+"| "
                
                strMatrix = strMatrix+"  %s%d  " % (" "*(pjgMax-len(str(kolom))),kolom)   
                    
                if baris.index(kolom) == len(baris)-1 :
                    strMatrix = strMatrix+" |\n"
                    
                
        return strMatrix
    
    
    @staticmethod
    def isSquare(listMatrix) :
        square = True
        if len(listMatrix) != len(listMatrix[0]) :
            square = False
    
        return square
    

    @staticmethod
    def addList(listMatrix1,listMatrix2) :
        pjgBaris = len(listMatrix1) == len(listMatrix2)
        pjgKolom = len(listMatrix1[0]) == len(listMatrix2[0])
    
    
        if pjgBaris and pjgKolom :
            hasil    = []
            for i in range(len(listMatrix1)) :
                tmpHasil = []
                for j in range(len(listMatrix1[i])) :
                    tmpHasil.append(listMatrix1[i][j]+listMatrix2[i][j])
    
                hasil.append(tmpHasil)
            return hasil
    
        else :
            print("'Ordo matrix tidak sama'")


