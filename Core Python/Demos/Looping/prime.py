# n=int(input("Enter number"))

# for i in range(2,n):
#     if(n%i==0):
#         print("Number is Not prime")
#         break
# else:
#     print("Number is prime")



    

# n=int(input("Enter number to check to prime"))
# if n>1:
#     for i in range(2,n):
#         if(n%i==0):
#             flag=False
#             break
#     if(flag==True):
#         print("Prime")
#     else:
#         print("not")
# else:
#     print(f"{n} is not prime number")

#print prime numbers between 1 to n
#first n prime numbers 

n=int(input("Enter limit :"))

for i in range(2,n):
    if(n%i==0):
        pass
    else:
        print(i,end=' ')

