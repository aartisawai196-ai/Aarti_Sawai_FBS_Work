#write a program to print list after removing all even numbers

li=[1,2,4,9,7,5,6]

for i in range(len(li)-1,-1,-1):
    if li[i]%2==0:
        li.remove(li[i])
print(f'After removing lsit : {li}')