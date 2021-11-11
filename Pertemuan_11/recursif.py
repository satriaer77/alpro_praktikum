def factorial(num):

    if num==0:
        temp=1
     
    else: 
        temp=1
        while num>=1:
            temp=temp*num
            num=num-1 

    return(temp)


a=int(input("==> Masukkan bilangan = "))
b=factorial(a)
print(a,"! =",b)
