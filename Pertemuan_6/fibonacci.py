ak1 = 0
ak2 = 1
ht = 0

def fibonacci(akg,a1,a2,htg) :
    hst=""
    while htg < akg:
       
      
       hst      = hst+str(a1)
       hasilf   = a1 + a2
       a1       = a2
       a2       = hasilf
       htg      = htg+1
    print(hst)

def fibonacciv2(akg,a1,a2,a3) :
    
    for i in range(akg) :
        print(a1)
        fib = a1+a2
        

def fibbonacci(n) :
    a = 0
    b = 1
    s=[]
    
    for i in range(n) :
        s.append(a)
        c = a + b
        a = b
        b = c
        
    return s

print(fibbonacci(10))


try:
    jmlAngka = int(input("==>Masukkan jumlah angka : "))

except:
    print("Yang anda masukkan bukan angka")

else:
    fibonacci(jmlAngka,ak1,ak2,ht)
