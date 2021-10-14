data    = input("==> Masukkan Kata/Kalimat : ")
vokal   = ['a','i','u','e','o']
kata    = ["",""]


for huruf in data :
    if huruf in vokal :
        kata[0] = kata[0]+" "+huruf
    
    else:
        kata[1] = kata[1]+" "+huruf

#if 'a' in data :
#    kata[0] = kata[0]+" "+'a'


jmlhuruf    = [len(kata[0].replace(" ","")),len(kata[1].replace(" ",""))]
spasi       = data.count(" ")       #Jumlah Spasi setiap huruf konsonan dan vokal [kata[0].count(" "),kata[1].count(" ")]


#print(kata[0]," ",jmlvokal,spasi)

print("""
    
    Jumlah Huruf Vokal      : %s, yaitu : %s
    Jumlah Huruf Konsonan   : %s, yaitu : %s 
    Jumlah Spasi            : %d

        """ % (jmlhuruf[0],kata[0],jmlhuruf[1],kata[1],spasi))
