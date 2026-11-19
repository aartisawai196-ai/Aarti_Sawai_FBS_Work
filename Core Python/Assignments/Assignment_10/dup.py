#write a progrm to create duplicate of existing list it should not point to same list

l1=[1,2,3,4,5]
l2=[]

for e in l1:
    l2.append(e)
    
print(l1,l2)
print(id(l1),id(l2))

