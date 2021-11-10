treshold = int(input("Masukkan Nilai :"))

data = [90, 56, 34, 78, 86, 90, 87, 88, 75, 65, 86, 57, 89, 67, 80] 
nl = ""
indeks = 0
for dt in data :
    if dt > treshold :
        nl=nl+" "+str(indeks)
    indeks+=1
print(nl)
