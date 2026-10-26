#write a program to print armstronge number within given range

start=int(input("Enter starting range"))
end=int(input("Enter ending range"))

for i in range(start,end+1):
    sum=0
    temp=i
    d=len(str(i))
    while temp>0:
        digit=temp%10
        sum+=digit**d
        temp=temp//10
    if(sum==i):
        print(i)