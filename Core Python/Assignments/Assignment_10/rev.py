#write a program to reverse a list
li=[1,2,3,4,5,9,7,8]
print(f'before reversing list :{li}')
rev=[]
for i in range(-1,-9,-1):
    rev.append(li[i])
    # print(rev)
print(f'reversed list ::{rev}')
