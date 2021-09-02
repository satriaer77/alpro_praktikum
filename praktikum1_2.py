
error = 0 #digunakan untuk menghitung kesalahan exception

        
        
#Fungsi formula Un

def mencariUn(a,b,n) :
   return a+(n-1)*b
    
#End Fungsi formula Un


#Fungsi formula Un

def mencariSn(a,b,n) :
   return n/2*(2*a+(n-1)*b)
    
#End Fungsi formula Un


#Jalankan
while True :
    try :
        aVal = int(input("Masukkan Nilai a :"))
        bVal = int(input("Masukkan Nilai b :"))
        nVal = int(input("Masukkan Nilai n :"))
    
    except :
        error = error+1
        if error >=3 :
            print("Terjadi Kesalahan harap jalankan lagi")
            break
        else :
            print("Data yang anda masukkan salah/bukan angka!, harap coba lagi")
        
    else :
        print("\n+===================+")
        
        for i in range(1,nVal+1) :
            print("U-",i," : ",mencariUn(aVal,bVal,i))
        
        print("Hasil Sn : ",mencariSn(aVal,bVal,nVal))
        cont = str(input("Anda ingin mengulang lagi ya/tidak : "))
        if cont == "ya" :
            print("+===================+\n\n")
            continue
        else :
            print("+======Selesai======+\n\n")
            break
