#list1 = [5,3,2,7]
#list2 = [6,2,6,7,8,9,2]
list1 = []
list2 = []
list3 = []
jmlList1 = int(input("==> Masukkan jumlah list1 : "))
jmlList2 = int(input("==> Masukkan jumlah list2 : "))


for i in range(jmlList1) : 
    list1.append(int(input("==> Masukkan data angka 1 : ")))

for i in range(jmlList2) :
    list2.append(int(input("==> Masukkan data angka 2 : ")))

#Tambahkan List
if len(list1) > len(list2) :
    for i in range(len(list1)) :
        if i < len(list2) :
            list3.append(list1[i]+list2[i])
        else :
            list3.append(list1[i])
    
else :
    for i in range(len(list2)) :
        if i < len(list1) :
            list3.append(list1[i]+list2[i])
        else :
            list3.append(list2[i])

print("""
list1 = %s
list2 = %s
list3 = %s
        """%(list1,list2,list3))
