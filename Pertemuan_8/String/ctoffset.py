a = input("Masukkan kata : ")

b = input("Cari huruf : ")
jm = 0
for g in a :
    if g == b :
        jm+=1


print("Jadi huruf %s yang ada di kata %s ada %d" % (b,a,jm))
