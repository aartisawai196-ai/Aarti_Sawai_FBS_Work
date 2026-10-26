#write a program to sum of all prime numbers between 1 to n
def prime(n):
    sum=0
    for num in range(1,n+1):
        for i in range(2,num):
            if(num%i==0):
                break
        else:
            sum+=num
    print("sum of prime numbers is :",sum)

n=int(input("Enter limit :"))
prime(n)