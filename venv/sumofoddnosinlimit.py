low=int(input("enter lower limit"))
up=int(input("enter upper limit"))

sum=0
if(low>up):
    print("error")
while(low<=up):
    if(low%2!=0):
        sum+=low
    low+=1
print(sum)