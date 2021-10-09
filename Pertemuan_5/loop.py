
def forLoop(angka) :
    for i in range(angka) :
        print("Angka ",i+1)

def forLoop1(angka) :
    for i in range(1,angka+1,1) :
        print("Angka ",i)



def whileLoop(angka):
    i=1
    while i <= angka :
        print("Angka ",i)
        i=i+1


def whileLoopBr(angka) :
    i = 1
    while True :
        if(i<=angka) :
            print("Angka ",i)
            i+=1
        else :
            break


try :
    angka = int(input("==> Masukkan angka : "))

except :
    print("Yang anda masukkan bukan angka")

else :
    forLoop1(angka)
