biner = input("==> Masukkan bilangan biner : ")[::-1]
total = 0
index = 0
    
for bi in biner :
    if bi == "1" :
        total = 2**index + total
    index+=1

print("""
+---------------->>
|>>>>>  Desimal : %d
+---------------->>
""" % (total))
