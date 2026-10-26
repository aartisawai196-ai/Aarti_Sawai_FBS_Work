#write a program to print fibonacci series

def fibo(n):
    a=-1
    b=1
    for i in range(1,n+1):
        c=a+b
        print(c,end=" ")
        a=b
        b=c

n=int(input("Enter limit :"))
fibo(n)