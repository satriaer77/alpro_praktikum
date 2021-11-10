jmlBil = int(input("masukkan jumlah bilangan : "))
i = 0
j = 0
total = 0
while True :
    
    if i%2!=0 :
        j+=1
        total = total+i
        print("Bilangan ke %d : %d"%(j,i))
    if j==jmlBil :
        break
    i+=1
print("Total = ",total)
