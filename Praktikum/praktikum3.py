data = "aKKKa"
vokal = ['a','i','u','e','o']
kata = ["",""]

for kont in data :
    if kont in vokal :
        kata[0] = kata[0]+" "+kont
    
    else:
        kata[1] = kata[1]+" "+kont


jmlvokal= len(kata[0].replace(" ",""))
spasi= kata[0].count(" ")
print(kata[0]," ",jmlvokal,spasi)
