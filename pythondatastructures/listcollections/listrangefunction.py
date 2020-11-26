lst=[2,3,4,6]#2**1=2,3**2=9,4**3=64,6**4=1296
cnt=1
val=[]
for i in lst:
    data=i**cnt
    val.append(data)
    cnt+=1
print(val)
    