#write  a program to sum of all odd numbers between 1 to n

def sumOdd(n):
    sum=0
    for i in range(1,n+1):
         sum+=i
    print(sum)


n=int(input("Enter limit :"))
sumOdd(n)