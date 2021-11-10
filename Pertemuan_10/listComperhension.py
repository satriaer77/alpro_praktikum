#List Compherhension

data    = [4,5,7,3,9,6,8,10]
bil     = [dt for dt in data  if dt%2==0 if dt<6]
print(bil)
