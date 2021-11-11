kalimat = input("==> Masukkan kalimat : ")
huruf   = input("==> Masukkan huruf yang dicari : ")
noHuruf = 1

for i in range(len(kalimat)) :
    if kalimat[i].lower() == huruf.lower() :
        print("Huruf %s atau huruf %s ke- %d : offset- %d"%(huruf.lower(),huruf.upper(),noHuruf,i))
        noHuruf+=1
