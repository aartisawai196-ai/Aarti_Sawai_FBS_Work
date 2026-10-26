#write a program to check whether given year is leap or not 

def year(y):
    if y%4==0 or y%400==0:
        print("given year is leap")
    elif(y%100==0):
        print("year is not leap")
    else:
        print("year is not leap")

y=int(input("Enter year"))
year(y)