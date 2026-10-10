# write a program to input angles of a triangle and check whether is valid or not
a=int(input("Enter First Angle of traingle :"))
b=int(input("Enter Second Angle of traingle :"))
c=int(input("Enter Third Angle of traingle :"))
sum=a+b+c
if sum==180:
    print("Traingle is Valid.")
else:
    print("Traingle is not valid.")