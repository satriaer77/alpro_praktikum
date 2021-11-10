lst     = [90, 56, 34, 78, 86, 90, 87, 88, 75, 65, 86, 57, 89, 67, 80] 
total   = 0

for l in lst :
    if l % 2 != 0 :
        total = total+l
        print(l)

print("Total : ",total)
