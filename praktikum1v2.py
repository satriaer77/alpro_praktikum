#Import library
import colorama
from colorama import Fore, Style

print(Fore.WHITE)
print(""" 
+===========================================================================+
 __      ____               _   _   _______   _   _   _   _    _   _      _ 
| _ \   |  _ \      /\     | | / / |__   __| | | | | / / | |  | | | \    / |
||_| |  | |_| |    /  \    | |/ /     | |    | | | |/ /  | |  | | |  \  /  |
| _ /   |    /    / /\ \   |   /      | |    | | |   /   | |  | | |   \/   |
| |     | |\ \   / ____ \  | |\ \     | |    | | | |\ \  | |__| | | |\__/| |
|_|     |_| \_\ /_/    \_\ |_| \_\    |_|    |_| |_| \_\ |______| |_|    |_|

+==========================================================================+

  ___
 /   |
/_/| |
   | |
 __| |__
|_______| 
   
""")
print(Style.RESET_ALL)


#Input Number
error = 0

#Fungsi untuk mencetak bilangan ganjil/genap ambil dari inputan pilihBilangan
def printAngka(angka,bilangan) :
    jumlah = 0
    print("o-----------o")
    for i in range(angka) :

        if i % 2 == 0 and bilangan == "genap" :
            print("| Angka ",i," |")
            jumlah = jumlah + i

        elif i % 2 != 0 and bilangan == "ganjil" :
            print("| Angka ",i," |")
            jumlah = jumlah + i
   
        if i == (angka-1) :
            print("o-----------o")
            print(Fore.LIGHTRED_EX +"Jumlah Keseluruhan Angka "+bilangan+"  : ",jumlah)
            print(Style.RESET_ALL)
            cont = str(input("Anda ingin mengulang lagi ya/tidak : "))
            if cont == "ya" :
                return 1
            else :
                return 0
        
        
#Jalankan     
while True :
    try :
        pilihBilangan  = str(input("Pilih Bilangan ganjil/genap :"))
               
        if pilihBilangan == "ganjil" or pilihBilangan == "genap" :
            jumlahAngka    = int(input("Masukkan Jumlah Angka : "))
            if printAngka(jumlahAngka,pilihBilangan) == 1 :
                continue
            else :
                break
        else :
            print("Kesalahan inputan pilih bilangan")
            break
                
                
        
    except :
        error = error + 1 
        if(error >= 3) : #Menghindari loop hole
            print("Terjadi Kesalahan harap jalankan lagi")
            break

        print("Yang anda masukkan bukan angka,Coba Lagi")
        
