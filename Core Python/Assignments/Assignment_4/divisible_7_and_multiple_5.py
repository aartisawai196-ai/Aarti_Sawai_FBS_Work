#write a program to find which numbers are divisible by 7 and multiple of 5 in given range

start=int(input("Enter starting range :"))
end=int(input("Enter ending range :"))

for i in range(start,end+1):
    if(i%7==0 and i%5==0):
        print(i)