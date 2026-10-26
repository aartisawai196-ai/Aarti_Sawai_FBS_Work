#write a program to print sum of series upto n
n=int(input("Enter limit :"))
sum=0
for i in range(1,n+1):
    sum+=i
print(f"Sum of series is {sum}")

