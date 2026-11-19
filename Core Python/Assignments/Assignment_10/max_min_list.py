#write a program to find maximum and minimum elements from list

li=[1,2,3,4,5,9,7,8]
max=li[0]
min=li[0]
for i in range(1,len(li)-1):
    if max<li[i]:
        max=li[i]
    elif min>li[i]:
        min=li[i]
print(f"maximum elements of list : {max}")
print(f"minimum elements of list : {min}")
