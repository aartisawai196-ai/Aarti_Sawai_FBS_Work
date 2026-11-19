#write a program to create a duplicate of existing list  it should not point to same list

l1=[1,2,3,4,5,6,7]
l2=[]
for i in range(len(l1)):
    l2.append(l1[i])
print(f'list 1 := {l1}')
print(f'list 2 := {l2}')

print(f'list 1 at {id(l1)} memory address')
print(f'list 2 at {id(l2)} memory address')
