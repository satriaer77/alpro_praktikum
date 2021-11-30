
banyakBab   = int(input("==> Masukkan banyak BAB : "))
bab         = []
subab       = []

#Memasukkan bab dan subab ke list menggunakan for loop
for i in range(banyakBab):
    
    bab.append(input("\n==> Masukkan BAB %d : "%(i+1))) #Menambahkan Bab ke list bab
    subab.append(input("-> Masukkan Subab : ")) #Meanmbahkan Subab ke list subab 



for i in range(len(subab)) :
    subab[i] = subab[i].split(",") #Membagi string menjadi potongan list sesuai argument yang dimasukkan


#Menampilkan isi list bab dan subbab
for i in range(len(bab)) :
    
    print("\nBAB %d : %s " %(i+1,bab[i])) #Menapmilkan BAB
    for j in range(len(subab[i])) : 
        print("   %d.%d : %s"% (i+1,j+1,subab[i][j])) #Menampilkan subab





