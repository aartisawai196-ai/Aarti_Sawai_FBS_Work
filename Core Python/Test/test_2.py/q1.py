year=int(input("Enter year :"))

if year%4==0:
    if year%100==0:
        if year%400==0:
            print("year is leap")
        else:
            print("not a leap year")

if(year%4==0):
    print("year is leap")
elif(year%100!=0):
    print("year is leap")
elif(year%400==0):
    print("year is leap")
else:
    print("not leap")