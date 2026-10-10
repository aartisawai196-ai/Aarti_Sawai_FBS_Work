#why-> To reduce code redundency
# what To execute block og code multiple number of times
# how 
#syntax

#initialization
# while(condition):
#     block of code

#write a program to sum of digit
n=int(input("Enter number"))
sum=0
while n>0:
    d=n%10
    sum+=d
    n=n//10
print(sum)