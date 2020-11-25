num1=int(input("enter 1st numbers\n"))
num2=int(input("enter 2nd number\n"))
num3=int(input("enter 3rd number\n"))

if((num1>num2)^(num1 >num3)):
    print("second largest number is",num1)
elif((num2 > num1) ^ (num2 > num3)):
    print("second largest number is",num2)
elif((num3>num1)^(num3>num2)):
    print("second largest number is",num3)
else:
    print("numbers are equal",num1)