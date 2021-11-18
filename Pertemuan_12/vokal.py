kalimat    = input("==> Masukkan Kata/Kalimat : ") 

def cekKonsonan(data) :
    vokal   = ['a','i','u','e','o']
  

    for huruf in data :
        if huruf.lower() in vokal : 
            print(data," adalah huruf vokal")
        else:
            print(data," adalah huruf konsonan")
   

cekKonsonan(kalimat)
