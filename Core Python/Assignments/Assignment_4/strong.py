#write a program ro check whether given number is strong or not.

n=int(input("Enter number :"))
temp=n
sum=0
while n>0:
    digit=n%10
    fact=1
    for i in range(1,digit+1):
        fact*=i
    sum+=fact
    n=n//10

if(temp==sum):
    print(f"{temp} is strong number")
else:
    print(f"{temp} is not strong")