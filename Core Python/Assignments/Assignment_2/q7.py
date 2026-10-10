# write a program to find sum of three digit number
num=int(input("Enter a number to find sum"))
s=0
while num>0:
    rem=num%10
    s=s+rem
    num=num//10

print("Sum is",s)