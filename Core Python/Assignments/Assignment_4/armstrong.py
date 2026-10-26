#write a program to check whether th numbers is armstrong or not

n=int(input("Enter number:"))
temp=n
digits=len(str(n))
sum=0
while n>0:
    digit=n%10
    sum+=digit**digits
    n=n//10

if(temp==sum):
    print("Number is armstrong !!")
else:
    print("Number is not armstrong !!")
