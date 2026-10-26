#write a program to find reverse of a number

def rev(n):
    re=0
    while n>0:
        d=n%10
        re=re*10+d
        n=n//10
    print("reverse of a number",re)

n=int(input("Enter number :"))

rev(n)