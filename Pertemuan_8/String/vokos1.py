data    = input("==> Masukkan Kata/Kalimat : ")
vokal   = "aiueo"
konsonan = "bcdfghjklmnpqrstvwxyz"
kns=""
jmlkonsonan = 0 
jmlvokal = 0
jmlSps = 0

for v in vokal :
    for dt in data :
        if v == dt :
            jmlvokal+=1
        
for k in konsonan :
    for dt in data :
        if k == dt :
            jmlkonsonan+=1

for dt in data :
    if  dt == ' ':
        jmlSps+=1
        


print("""
    
    Jumlah Huruf Vokal      : %d 
    Jumlah Huruf Konsonan   : %d 
    Jumlah Spasi            : %d

        """ % (jmlvokal,jmlkonsonan,jmlSps))

