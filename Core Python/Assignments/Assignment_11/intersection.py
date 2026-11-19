#write a program to find intersection of two list
l1=[1,2,3,5,4,6]
l2=[2,3,5,8,9,98]
inter=[]
for i in range(len(l1)):
    for j in range(len(l2)):
        if l1[i]==l2[j]:
            inter.append(l1[i])
print(f'intersection of list is {inter}')
            