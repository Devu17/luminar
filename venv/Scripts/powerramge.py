num=int(input("enter number"))
i=0
sum=0
p=0
while(i<num):

    p=p+((10**i)*num)
    sum+=p
    i += 1

print(sum)