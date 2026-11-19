#write a program to put even and odd elements of a list into two different lists
li=[1,2,3,4,5,6,7,8,9,10]
even=[]
odd=[]
for i in range(len(li)):
    if li[i]%2==0:
        even.append(li[i]) 
    else:
        odd.append(li[i])
print(f'Original list {li}')
print(f'Even list {even}')
print(f'Odd list {odd}')
