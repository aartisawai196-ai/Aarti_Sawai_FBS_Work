#write a program to print all numbers are divisible by m and n in the list

li=[1,4,6,7,9,90,78,45,23]
m=int(input("Enter the value of m :"))
n=int(input("Enter the value of n :"))

for i in range(len(li)):
    if(li[i]%m==0 and li[i]%n==0):
        print(li[i])