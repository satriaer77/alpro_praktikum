bab     = int(input("==> Masukkan jumlah BAB = "))
subab   = int(input("==> Masukkan jumlah SUB BAB di setiap BAB = "))

for i in range(1,bab+1) :
    print("BAB ",i)
    for j in range(1,subab+1) :
        print("  SUB BAB %d.%d"%(i,j))
