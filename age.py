bday=input("enter ur bday")
cday=input("enter current year")
print(bday)
print(cday)
bdate,bmonth,byear=bday.split("-")
cdate,cmonth,cyear=cday.split("-")
age=int(cyear)-int(byear)
print(age)
if(cmonth<=bmonth):
    if(cdate<bday):
        age-=1
print("ur age",age,"year old")