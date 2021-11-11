kalimat    = input("==> Masukkan Kata/Kalimat : ") 

def cekKonsonan(data) :
    vokal   = ['a','i','u','e','o']
    kata    = ["",""]  

    for huruf in data.replace(" ","") :
        if huruf.lower() in vokal : 
            kata[0] = kata[0]+" "+huruf
        else:
            kata[1] = kata[1]+" "+huruf
    return kata

huruf       = cekKonsonan(kalimat)
jmlhuruf    = [len(huruf[0].replace(" ","")),len(huruf[1].replace(" ",""))]


print("""
    
    Jumlah Huruf Vokal      : %s, yaitu : %s
    Jumlah Huruf Konsonan   : %s, yaitu : %s 
  

        """ % (jmlhuruf[0],huruf[0],jmlhuruf[1],huruf[1]))
