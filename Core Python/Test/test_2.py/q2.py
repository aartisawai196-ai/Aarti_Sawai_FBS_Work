n=int(input("Enter number"))
d1=n%10
num=n//10
d2=num%10
no=num//10
d3=no%10
nn=no//10
if (d3==2*d2 and d3==int(0.5*d1)):
    print("yes, you have done it")
else:
    print("Please try next time")
