lst=[1,2,3,4,6,7]#value=6(4,2) print pair
value=int(input("enter value"))
for i in lst:
    for j in lst:
        if(j+i==value):
            print(j,i)