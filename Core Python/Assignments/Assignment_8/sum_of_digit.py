#write a program to find sum of digit

def sumOfdigit(n):
    sum=0
    while n>0:
        digit=n%10
        sum+=digit
        n=n//10
    print("sum of digits :",sum)

n=int(input("Enter number :"))
sumOfdigit(n)