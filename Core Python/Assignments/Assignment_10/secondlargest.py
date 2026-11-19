#write a program to find second largest elements from the list

li=[1,2,3,4,5,9,7,8]
max=li[0]
secmax=li[0]
for i in range(1,len(li)):
    if max<li[i]:
        secmax=max
        max=li[i]
    elif max>li[i] and li[i]!=secmax:
        secmax=li[i]
print(f"maximum elements of list : {max}")
print(f"second maximum elements of list : {secmax}")