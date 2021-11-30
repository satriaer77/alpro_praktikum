def createList(panjanglist) :
    angka=[]
    for i in range(panjanglist) :
        akg=int(input('Masukkan data ke- '+str(i)+' : '))
        angka.append(akg)

    return angka


def avgList(angkalist) :
    total=0
    for i in range(len(angkalist)) :
        total=total+angkalist[i]

    return total/len(angkalist)

def addList(l1,l2) :
    l3=[]
    for i in range(len(l1)) :
        l3.append(l1[i]+l2[i])

    return l3


data1=createList(5)
print('data 1 = ',data1,' ; rata-rata list : ',avgList(data1))
data2=createList(5)
print('data 2 = ',data2,' ; rata-rata list : ',avgList(data2))
hasil=addList(data1,data2)
print(data1,'+',data2,'=',hasil)


