#write a program of having n number having n number of elements in a list and find out even
# and odd elemnts in that list and then create separte lists which will have
# even elements and other will have odd elments

n=int(input("how many numbers do you want in a list :"))
li=[]
even=[]
odd=[]
for i in range(1,n+1):
    num=int(input(f"Enter {i} no tu add in a list"))
    li.append(num)
for i in range(len(li)):
    if li[i]%2==0:
        even.append(li[i])
    else:
        odd.append(li[i])
print(f'List is :{li}')
print(f'Even list is {even}')
print(f'odd list is {odd}')
    