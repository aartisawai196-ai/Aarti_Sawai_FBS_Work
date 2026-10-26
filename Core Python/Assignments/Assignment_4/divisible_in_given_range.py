#write a program to print all numbers in a range divisible by given number
n=int(input("Enter number :"))
start=int(input("Enter starting range :"))
end=int(input("Enter ending range :"))

for i in range(start,end+1):
    if(n%i==0):
        print(i)
