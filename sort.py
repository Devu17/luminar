num1 = int(input("enter num1"))
num2 = int(input("enter num2"))
num3 = int(input("enter num3"))
if((num1>num2)or(num1>num3)):
    print("num1 is max")
    if(num2>num3):
        print(num1,",",num2,",",num3)
    else:
        print(num1,",",num3,",",num2)
elif((num2>num1)or(num2>num3)):
    print("num2 is max")
elif ((num3 > num1) or (num3 > num2)):
    print("num3 is max")

