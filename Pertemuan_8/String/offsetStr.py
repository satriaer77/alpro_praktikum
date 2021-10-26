kata = input("Masukkan kata : ")
cari = input("Cari : ")
bnyk = len(kata)

for a in range (bnyk):
    print("offset - ",a,"huruf ",kata[a])

for k in kata:
    print(k)

print(kata.find(cari))
print("Karakter terakhir : ",kata[-1])
