#write a program to remove duplicates from list

li=[8,4,2,7,2,4,3,4,5,9,1]
unique_list=[]

for i in range(len(li)):
        if li[i] not in unique_list:
            unique_list.append(li[i])
print(f'unique list :{unique_list}')
