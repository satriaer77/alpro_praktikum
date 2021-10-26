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



binerDesimal()
