#write a program to print first n prime numbers

n=int(input("Enter numbers..!"))
count=1
while count<n:
    for num in range(1,n):
        for i in range(2,num):
            if(num%i==0):
                break
        else:
            print(num)
            count+=1
  