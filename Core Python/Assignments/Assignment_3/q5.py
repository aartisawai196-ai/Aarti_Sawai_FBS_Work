a=int(input("Enter  value of a:"))
b=int(input("Enter  value of b:"))
c=int(input("Enter  value of c:"))
if(a==b==c):
    print("Traingle is Equilateral")
elif(a==b or b==c or c==a):
    print("Traingle is Isoceles")
else:
    print("Traingle is scalene")