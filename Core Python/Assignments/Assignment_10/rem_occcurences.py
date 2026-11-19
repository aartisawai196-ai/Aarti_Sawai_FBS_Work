#write a program to remove all occurences of given elements in the list

li=[1,4,5,4,6,7,4,2,6]
print(f'before removing :{li}')
n=int(input("Enter number to remove occurences :"))
i=0
while i<len(li):
    if li[i]==n:
        li.remove(li[i])
    i+=1
print(f'After romoving all occurences of {n} : {li}')
