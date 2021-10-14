def desimalBiner() :
    try : 
        convBiner = ""
        desimal = int(input("Masukkan bilangan desimal : "))
    except :
        print("Yang anda masukkan bukan angka")
    else :
        while True :
            biner       = desimal % 2
            desimal     = desimal // 2
            convBiner   = str(biner)+convBiner
            print(biner)
            if desimal == 1 :
                print(1)
                convBiner = "1"+convBiner
                print("Biner : ",convBiner)
                break




def binerDesimal() :
    biner = input("Masukkan bilangan biner : ")[::-1]
    total = 0
    index = 0
    
    for bi in biner :
        if bi == "1" :
            total = 2**index + total
            #print(total)
        index+=1

    print("Desimal : ",total)




while True :
    try : 
        print("""

Menu
----
1.) Tekan 1 untuk konversi desimal ke biner
2.) Tekan 2 untuk konversi biner ke desimal


                """)
        pilih = int(input("==> Masukkan Pilihan anda : "))

    except : 
        print("Yang anda masukkan bukan angka")

    else :

        if pilih == 1 : 
            desimalBiner()
        elif pilih == 2 :
            binerDesimal()
           
        else :
            print("Yang anda masukkan tidak ada di menu")

        
        lanjut = input("Apakah anda ingin melanjutkan program y/t : ")

        if lanjut == "t" :
            break
