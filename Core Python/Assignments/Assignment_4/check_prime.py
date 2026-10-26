#write a program to check if given number is prime or not

n=int(input("Enter number to check :"))
flag=True
if(n>0):
    for i in range(2,n):
        if(n%i==0):
            flag=False
            break
        else:
            flag=True
    if(flag==True):
        print(f"{n} is Prime number.")
    else:
        print(f"{n} is not prime number.")
else:
    print("You entered Invalid number !!")