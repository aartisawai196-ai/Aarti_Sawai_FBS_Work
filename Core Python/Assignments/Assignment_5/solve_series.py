#write a program to solve following series
# 1!+2!+3!+4!.......n!

n=int(input("Enter number"))
sum=0
fact=1
for num in range(1,n):
    for i in range(1,num+1):
        fact+=num*i
print(fact)