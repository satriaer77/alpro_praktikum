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
        if desimal == 0 :
            print("Biner : ",convBiner)
            break


