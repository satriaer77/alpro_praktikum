
data = [90, 56, 34, 78, 86, 90, 87, 88, 75, 65, 86, 57, 89, 67, 80] 

while True:
    print("""
===Menu===
1. AVG
2. MAX
3, Indeks dari list yang lebih dari treshold
""") 
    pilih = int(input("Masukkan Pilihan (1/2/3) : "))
    
    
    if pilih == 1 :
        total = 0
        for dt in data :
            total = total+dt
        print("Rata-rata : ",total/len(data))

    elif pilih == 2 :
        maks = data[0]
        for d in data:
            if maks < d :
                maks = d

        print(maks)
    elif pilih == 3 :
        treshold = int(input("Masukkan Nilai :"))

        nl = ""
        indeks = 0
        for dt in data :
            if dt > treshold :
                nl=nl+" "+str(indeks)
            indeks+=1
        print(nl)
        
    else :
        print("Yang anda pilih tidak ada di menu")

    #Ulang Lagi Atau tidak
    lj = input("Lanjut lagi y/n :")
    if lj == 'n' :
        break
