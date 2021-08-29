##### #Import library
import colorama
from colorama import Fore, Style

print(Fore.WHITE)
print(""" 
+==========================================================================+
 __      ____               _   _   _______   _   _   _   _    _   _      _ 
| _ \  |  _ \      /\     | | / / |__   __| | | | | / / | |  | | | \    / |
||_| | | |_| |    /  \    | |/ /     | |    | | | |/ /  | |  | | |  \  /  |
| _ /  |    /    / /\ \   |   /      | |    | | |   /   | |  | | |   \/   |
| |    | |\ \   / ____ \  | |\ \     | |    | | | |\ \  | |__| | | |\__/| |
|_|    |_| \_\ /_/    \_\ |_| \_\    |_|    |_| |_| \_\ |______| |_|    |_|

+==========================================================================+

  ___
 /   |
/_/| |
   | |
 __| |__
|_______| 
   
""")
print(Style.RESET_ALL)


error = 0 #digunakan untuk menghitung kesalahan exception


#Fungsi untuk mencetak bilangan ganjil ambil dari inputan jumlahAngka
def printAngkaGanjil(angka) :
    jumlah = 0
    print("o-----------o")
    for i in range(angka) :
        if i % 2 != 0 :
            print("| Angka ",i," |")
            jumlah = jumlah + i
   
        if i == (angka-1) :
            print("o-----------o")
            print(Fore.LIGHTRED_EX +"Jumlah Keseluruhan Angka Ganjil : ",jumlah)
            print(Style.RESET_ALL)
            cont = str(input("Anda ingin mengulang lagi ya/tidak : "))
            if cont == "ya" :
                return 1
            else :
                return 0
#End Fungsi printAngkaGanjil        
        
    
    
#Jalankan     
while True :
    try :
        jumlahAngka    = int(input("Masukkan Jumlah Angka : "))
        if printAngkaGanjil(jumlahAngka) == 1 :
            continue
        else :
            break
                
                   
    except :
        error = error + 1
        if error >= 3 : 
            print("Terjadi Kesalahan harap jalankan kembali")
            break
        else :
            print("Yang anda masukkan bukan angka,Coba Lagi")
    



