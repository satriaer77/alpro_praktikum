class Matrix() :

    #----- Fungsi Membuat Matrix (createMatrix) -----#
    # argument menggunakan variable baris dan kolom tipe <int>
    # return value list matrix
    
    @staticmethod
    def createMatrix2D(baris,kolom) :
        print("\nBuat Matrix Ordo %d x %d " % (baris,kolom) )
        matrix = []
        for i in range(baris) :
            bar = [] 
            for j in range(kolom) :
                bar.append(int(input("==> Mat[%d,%d] : " % (i,j) ))) #Menambahkan element inputan user <int> ke list bar
                
            matrix.append(bar) #Add element list bar ke list matrix
    
        return matrix
    
    #----- End Fungsi Membuat List Matrix  (createMatrix) -----#
    
    
    
    
    #----- Fungsi Menampilkan Matrix (dispMatrix2D) -----#
    # argument menggunakan variable list matrix
    # return value string
    
    @staticmethod
    def dispMatrix2D(listMatrix) :
        strMatrix = ""
        pjgMax    = 0 #Menampung nilai panjang karakter nilai terbesar
        
        #Mencari panjang karakter dari nilai terbesar
        for i in range(len(listMatrix)) : 
            if pjgMax < len(str(max(listMatrix[i]))) :              
                pjgMax = len(str(max(listMatrix[i])))
        
        #Menggabungkan string ke strMatrix
        for baris in listMatrix :
            i =  0 #Meghitung index
            for kolom in baris :
                
                if i == 0 : #cek bila index sama dengan 0
                    strMatrix = strMatrix+"| "
                    
                strMatrix = strMatrix+"  %s%d  " % (" "*(pjgMax-len(str(kolom))),kolom)   
                        
                if i == len(baris)-1 : #Cek bila index sama dengan index terakhir dari baris
                    strMatrix = strMatrix+" |\n"
                    
                i+=1
                    
        return strMatrix
    
    #----- End Fungsi Menampilkan Matrix (dispMatrix2D) -----#
    
    
    
    
    #----- Fungsi Mengecek Apakah Panjang Baris dan Kolom Matrix Sama -----#
    # argument menggunakan variable list matrix
    # return value boolean
    
    @staticmethod
    def isSquare(listMatrix) :
        square = True
        if len(listMatrix) != len(listMatrix[0]) :
            square = False
    
        return square
    
    #----- End Fungsi Mengecek Apakah Panjang Baris dan Kolom Matrix Sama (isSquare) -----#
    
    
    
    
    #----- Fungsi Menjumlahkan 2 Matrix Sama Ordo (addList) -----#
    # argument menggunakan variable 2 list matrix
    # return value hasil penjumlahan matrix <list>
    
    @staticmethod
    def addList(listMatrix1,listMatrix2) :
        pjgBaris = len(listMatrix1) == len(listMatrix2) #Membandingkan panjang baris kedua matrix
        pjgKolom = len(listMatrix1[0]) == len(listMatrix2[0]) #Membangdingkan panjang kolom kedua matrix
    
    
        if pjgBaris and pjgKolom : #Jika Kedua Panjang baris dan kolom matrix sama
            hasil    = []
            for i in range(len(listMatrix1)) :
                tmpHasil = []
                for j in range(len(listMatrix1[i])) :
                    tmpHasil.append(listMatrix1[i][j]+listMatrix2[i][j]) #Menambahkan hasil penjumlahhan kedua element matrix ke list tmpHasil
    
                hasil.append(tmpHasil) #Menambahkan element tmpHasil ke list hasil
    
            return hasil
    
        else :
            print("'Ordo matrix tidak sama'")
    
    #----- End Fungsi Menjumlahkan 2 Matrix Sama Ordo (addList) -----#
    
