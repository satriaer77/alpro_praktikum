import timg

def checkCase(cov) :

    if cov <= 5000:
        return "Green Zone"
    elif cov <= 15000 :
        return "Yellow Zone"
    elif cov <= 20000:
        return "Orange Zone"
    elif cov <= 25000 :
        return "Red Zone"
    else :
        return "Black Zone"
    






#-------------------------

#Jalankan
try :

    covCase = int(input("==> Masukkan jumlah pasien covid 19 : ")) #ambil data dari inputan user dengan tipe data int
   
except:#tampilkan ini bila yang user masukkan bukan angka

    print("Yang anda masukkan bukan angka")

else:
    print("""  
                ____      _______
               <oooo>    /ooooooo|   <>      ___    
    _      /oooooooo\    ||  ____   ;;      /   \______/\______  
   \o\     \oooooooo/    \ \/oo_/  .;  ,,   \__               |
    \o\     |oooooo/      \ooo/                \              | 
     \o\     _______      / /\ \   ./; ;;       \             |
      \_\   /______/ <o> /_/  \_\                \_____________\

    == Daerah anda termasuk daerah %s ==
            
        
    """ % (checkCase(covCase)))
