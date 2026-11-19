#write a program to create a new list from an existing list which contains cube of ach number of the list

li=[1,2,4,6,7,9]
cube=[]

for i in range(len(li)):
    cube.append(li[i]**3)
print(f"cube list := {cube}")
