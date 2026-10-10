# write a program to input all sides of a tiangle and check whether triangle is valid or not.
a=int(input("Enter side :"))
b=int(input("Enter side :"))
c=int(input("Enter side :"))

if(a+b>c and a+c>b and b+c>a):
    print("Traingle is Valid.")
else:
    print("Traingle is not valid.")