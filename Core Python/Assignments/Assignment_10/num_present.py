#write a program to accept number from user and check if this elements is present in the lsit or not 
#also tell how many times it is present in the list
li=[8,4,2,7,2,4,3,4,5,9,1]
num=int(input("Enter number do you want to search :"))
count=0
present=False
for i in range(len(li)-1):
    if li[i]==num:
        present=True
        count+=1
if present==True:
    print(f'{num} is found {count} times!!')
else:
    print(f'{num} is not found !!')
        
    